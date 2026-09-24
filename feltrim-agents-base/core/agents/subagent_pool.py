import asyncio
import logging
import uuid
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Type

logger = logging.getLogger(__name__)

class SubagentTask:
    def __init__(self, task_type: str, payload: Dict[str, Any]):
        self.task_id = str(uuid.uuid4())
        self.task_type = task_type
        self.payload = payload
        self.status = "PENDING"
        self.result = None
        self.error = None

class BaseSubAgent(ABC):
    def __init__(self, llm=None, log_callback=None, update_callback=None):
        self.llm = llm
        self.log_callback = log_callback
        self.update_callback = update_callback

    def log(self, msg: str):
        if self.log_callback:
            self.log_callback(msg)
        else:
            logger.info(msg)

    @abstractmethod
    async def process(self, task: SubagentTask) -> Any:
        pass

class TestWriterAgent(BaseSubAgent):
    async def process(self, task: SubagentTask) -> str:
        self.log(f"💭 [AI Thought]: {self.__class__.__name__} analyzing task: {task.payload.get('desc')}")
        if self.llm:
            prompt = f"You are an expert QA Engineer. Write clean pytest code for: {task.payload.get('desc')}"
            response = await asyncio.to_thread(self.llm.invoke, prompt)
            return response.content if hasattr(response, 'content') else str(response)
        await asyncio.sleep(0.1)
        return "Tests generated successfully with smart waits (Mocked)."

class DocUpdaterAgent(BaseSubAgent):
    async def process(self, task: SubagentTask) -> str:
        self.log(f"💭 [AI Thought]: {self.__class__.__name__} analyzing task: {task.payload.get('desc')}")
        if self.llm:
            prompt = f"You are a Technical Writer. Update the markdown documentation for: {task.payload.get('desc')}"
            response = await asyncio.to_thread(self.llm.invoke, prompt)
            return response.content if hasattr(response, 'content') else str(response)
        await asyncio.sleep(0.1)
        return "Documentation updated and markdown generated (Mocked)."

class RefactorAgent(BaseSubAgent):
    async def process(self, task: SubagentTask) -> str:
        self.log(f"💭 [AI Thought]: {self.__class__.__name__} analyzing task: {task.payload.get('desc')}")
        if self.llm:
            prompt = f"You are a Software Architect. Refactor this requirement into clean code: {task.payload.get('desc')}"
            response = await asyncio.to_thread(self.llm.invoke, prompt)
            return response.content if hasattr(response, 'content') else str(response)
        await asyncio.sleep(0.1)
        return "Code refactored applying clean architecture (Mocked)."

class SubagentRegistry:
    def registry(self) -> dict[str, type[BaseSubAgent]]:
        """Retorna o dicionário de agentes registrados no sistema."""
        if not hasattr(self, "_registry"):
            self._registry = {
                "test": TestWriterAgent,
                "doc": DocUpdaterAgent,
                "refactor": RefactorAgent,
            }
        return self._registry

    def register(self, name: str, agent_class: type[BaseSubAgent]) -> None:
        """Registra uma nova classe de subagente no sistema dinamicamente."""
        self.registry()[name] = agent_class
        logger.info(f"Subagente '{name}' ({agent_class.__name__}) registrado com sucesso.")

class SubAgentPool:
    """Gestor de fila assíncrona centralizada e execução isolada (Nível 6)."""
    def __init__(self, llm=None, log_callback=None, update_callback=None):
        self.queue: asyncio.Queue[SubagentTask] = asyncio.Queue()
        self.registry = SubagentRegistry()
        self._workers: List[asyncio.Task] = []
        self._stop_event = asyncio.Event()
        self.llm = llm
        self.log_callback = log_callback
        self.update_callback = update_callback

    async def submit_task(self, task_type: str, payload: Dict[str, Any]) -> SubagentTask:
        task = SubagentTask(task_type, payload)
        await self.queue.put(task)
        logger.info(f"Task {task.task_id} ({task_type}) enfileirada.")
        return task

    async def _worker_loop(self):
        while not self._stop_event.is_set():
            try:
                task = await asyncio.wait_for(self.queue.get(), timeout=1.0)
            except asyncio.TimeoutError:
                continue
            
            try:
                task.status = "PROCESSING"
                agent_class = self.registry.registry().get(task.task_type)
                if not agent_class:
                    raise ValueError(f"Agente para '{task.task_type}' não encontrado.")
                
                agent = agent_class(llm=self.llm, log_callback=self.log_callback, update_callback=self.update_callback)
                if self.update_callback:
                    self.update_callback(agent_class.__name__, "PROCESSING", {"task_id": task.task_id})
                
                task.result = await agent.process(task)
                task.status = "COMPLETED"
                
                if self.update_callback:
                    self.update_callback(agent_class.__name__, "COMPLETED", {"task_id": task.task_id})
            except Exception as e:
                task.status = "FAILED"
                task.error = str(e)
                logger.error(f"Task {task.task_id} falhou isoladamente: {e}")
            finally:
                self.queue.task_done()

    def start(self, num_workers: int = 3):
        self._stop_event.clear()
        for _ in range(num_workers):
            worker = asyncio.create_task(self._worker_loop())
            self._workers.append(worker)

    async def wait_for_all(self):
        """Aguarda todas as tarefas da fila concluírem e retorna status granular."""
        await self.queue.join()

    async def teardown(self):
        self._stop_event.set()
        await asyncio.gather(*self._workers, return_exceptions=True)
        self._workers.clear()
