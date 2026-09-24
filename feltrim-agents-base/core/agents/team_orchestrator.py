import asyncio
import logging
import uuid
from typing import Any, Dict, List, Optional
from .subagent_pool import SubAgentPool

logger = logging.getLogger(__name__)

class SharedTask:
    def __init__(self, description: str):
        self.task_id = str(uuid.uuid4())
        self.description = description
        self.state = "CREATED" # CREATED -> CLAIMED -> PROCESSING -> SYNCED -> FAILED
        self.history: List[str] = []
        self.result = None
        self.attempts = 0

class EndlessPoolState:
    """Implementa o conceito de Endless Pool, comprimindo histórico para economizar tokens."""
    def __init__(self, llm=None, log_callback=None):
        self.raw_history: List[str] = []
        self.summarized_context: str = ""
        self.TOKEN_THRESHOLD = 20 # Simulação de limite de tokens para compressão
        self.llm = llm
        self.log_callback = log_callback

    async def append_event_async(self, event: str):
        self.raw_history.append(event)
        if len(self.raw_history) >= self.TOKEN_THRESHOLD:
            await self.summarize_state_async()

    async def summarize_state_async(self):
        if self.log_callback:
            self.log_callback("💭 [AI Thought]: [EndlessPool] Atingiu limite de tokens. Comprimindo histórico via LLM...")
        else:
            logger.info("[EndlessPool] Atingiu limite de tokens. Comprimindo histórico...")
        
        if self.llm:
            prompt = "Summarize the following system events tightly:\n" + "\n".join(self.raw_history)
            import asyncio
            response = await asyncio.to_thread(self.llm.invoke, prompt)
            summary = response.content if hasattr(response, 'content') else str(response)
        else:
            summary = f"Summary of {len(self.raw_history)} events: Tasks progressed to SYNCED (Mocked)."
        
        self.summarized_context += "\n" + summary
        self.raw_history.clear()

class TeamLeadAgent:
    def __init__(self, pool: SubAgentPool, llm=None, log_callback=None):
        self.pool = pool
        self.llm = llm
        self.log_callback = log_callback
        self.endless_pool = EndlessPoolState(llm=llm, log_callback=log_callback)

    async def route_task(self, task: SharedTask):
        await self.endless_pool.append_event_async(f"Routing task: {task.description}")
        
        if self.log_callback:
            self.log_callback(f"💭 [AI Thought]: TeamLeadAgent is routing task: {task.description}")
            
        if self.llm:
            prompt = f"Given the task description: '{task.description}', respond ONLY with one of the following exact types: 'test', 'doc', 'refactor'."
            import asyncio
            response = await asyncio.to_thread(self.llm.invoke, prompt)
            content = response.content if hasattr(response, 'content') else str(response)
            task_type = content.strip().lower()
            if task_type not in ["test", "doc", "refactor"]:
                task_type = "refactor" # Fallback
        else:
            if "test" in task.description.lower():
                task_type = "test"
            elif "doc" in task.description.lower():
                task_type = "doc"
            else:
                task_type = "refactor"

        task.state = "CLAIMED"
        sub_task = await self.pool.submit_task(task_type, {"desc": task.description})
        return sub_task

class AgentTeamOrchestrator:
    """Nível 7: Orquestrador central com gerenciamento de handoffs e detecção de deadlocks."""
    def __init__(self, llm=None, log_callback=None, update_callback=None):
        self.llm = llm
        self.log_callback = log_callback
        self.update_callback = update_callback
        self.pool = SubAgentPool(llm=llm, log_callback=log_callback, update_callback=update_callback)
        self.team_lead = TeamLeadAgent(self.pool, llm=llm, log_callback=log_callback)
        self.active_tasks: List[SharedTask] = []
        self.MAX_ATTEMPTS = 3

    async def execute_team_sprint(self, task_descriptions: List[str]):
        self.pool.start(num_workers=3)
        
        for desc in task_descriptions:
            st = SharedTask(desc)
            self.active_tasks.append(st)

        # Dispatch
        pending_subtasks = []
        for task in self.active_tasks:
            sub = await self.team_lead.route_task(task)
            task.state = "PROCESSING"
            pending_subtasks.append((task, sub))

        # Deadlock detector loop with smart waits
        deadlock_timeout = 5.0
        start_time = asyncio.get_event_loop().time()
        
        while pending_subtasks:
            current_time = asyncio.get_event_loop().time()
            if current_time - start_time > deadlock_timeout:
                logger.warning("Deadlock detectado no Handoff! Recalculando...")
                break # Evita loop infinito

            for t_pair in pending_subtasks[:]:
                shared_t, sub_t = t_pair
                if sub_t.status in ["COMPLETED", "FAILED"]:
                    if sub_t.status == "COMPLETED":
                        shared_t.state = "SYNCED"
                        shared_t.result = sub_t.result
                    else:
                        shared_t.state = "FAILED"
                        shared_t.history.append(f"Erro: {sub_t.error}")
                    
                    await self.team_lead.endless_pool.append_event_async(f"Task {shared_t.task_id} mudou para {shared_t.state}")
                    pending_subtasks.remove(t_pair)
            
            await asyncio.sleep(0.5)

        await self.pool.wait_for_all()
        await self.pool.teardown()
        
        # Fazer um flush final se sobrou algo no pool (Endless Pool rule)
        if len(self.team_lead.endless_pool.raw_history) > 0:
            await self.team_lead.endless_pool.summarize_state_async()
            
        if self.log_callback:
            self.log_callback("🏁 Sprint concluída. Relatório Consolidado do Endless Pool gerado.")
        else:
            logger.info("Sprint concluída. Relatório Consolidado do Endless Pool gerado.")
        return self.team_lead.endless_pool.summarized_context
