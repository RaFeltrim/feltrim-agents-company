import asyncio
import pytest
from core.agents.team_orchestrator import AgentTeamOrchestrator

@pytest.mark.asyncio
async def test_team_orchestrator_execution():
    """Valida o orquestrador do Nível 7: roteamento, processamento paralelo e endless pool"""
    orchestrator = AgentTeamOrchestrator()
    
    tasks = [
        "Create the user login test",
        "Update the API docs",
        "Refactor the authentication module"
    ]
    
    summary = await orchestrator.execute_team_sprint(tasks)
    
    # Valida se o resumo consolidado foi gerado com sucesso
    assert "SYNCED" in summary or len(orchestrator.team_lead.endless_pool.raw_history) > 0
    
    # Valida se as tasks foram concluídas
    for shared_task in orchestrator.active_tasks:
        assert shared_task.state == "SYNCED"
        assert shared_task.result is not None
