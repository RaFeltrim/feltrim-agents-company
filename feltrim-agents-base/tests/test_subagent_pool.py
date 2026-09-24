import asyncio
import pytest
from core.agents.subagent_pool import SubAgentPool

@pytest.mark.asyncio
async def test_subagent_pool_initialization():
    """Valida o ciclo de vida do pool (start/stop)"""
    pool = SubAgentPool()
    pool.start(num_workers=1)
    assert len(pool._workers) == 1
    await pool.teardown()
    assert len(pool._workers) == 0

@pytest.mark.asyncio
async def test_subagent_pool_executes_tasks():
    """Tarefas são enfileiradas, processadas em paralelo e concluídas"""
    pool = SubAgentPool()
    pool.start(num_workers=3)
    
    t1 = await pool.submit_task("test", {"desc": "Escrever teste"})
    t2 = await pool.submit_task("doc", {"desc": "Atualizar docs"})
    
    await pool.wait_for_all()
    await pool.teardown()
    
    assert t1.status == "COMPLETED"
    assert t2.status == "COMPLETED"
    assert t1.result == "Tests generated successfully with smart waits."
    assert t2.result == "Documentation updated and markdown generated."

@pytest.mark.asyncio
async def test_subagent_pool_fault_isolation():
    """Falha isolada não propaga para outras tarefas (fail-fast por task)"""
    pool = SubAgentPool()
    pool.start(num_workers=2)
    
    # Simula uma task que vai falhar enviando um tipo não registrado
    t_fail = await pool.submit_task("invalid_type", {})
    t_success = await pool.submit_task("refactor", {"desc": "Refatorar módulo"})
    
    await pool.wait_for_all()
    await pool.teardown()
    
    assert t_fail.status == "FAILED"
    assert "não encontrado" in str(t_fail.error)
    
    # Valida que o erro da primeira NÃO derrubou o worker que processou a segunda
    assert t_success.status == "COMPLETED"
