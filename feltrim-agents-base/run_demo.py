import asyncio
import logging
import sys

# Configura o logger para imprimir no terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler(sys.stdout)])

from core.agents.team_orchestrator import AgentTeamOrchestrator

async def main():
    print("="*60)
    print("🚀 INICIANDO VALIDAÇÃO DE ORQUESTRAÇÃO NÍVEL 7")
    print("="*60)
    
    orchestrator = AgentTeamOrchestrator()
    
    # Simula as requisições que viriam do Master Orchestrator ou do Front-End
    tasks = [
        "Criar testes unitários para a validação de CNPJ (TestWriter)",
        "Refatorar o módulo de autenticação usando Clean Code (Refactor)",
        "Atualizar o CHANGELOG e a doc de Token Economy (DocUpdater)"
    ]
    
    summary = await orchestrator.execute_team_sprint(tasks)
    
    print("="*60)
    print("✅ EXECUÇÃO FINALIZADA")
    print("📋 RESUMO DO ENDLESS POOL:")
    print(summary)
    print("="*60)

if __name__ == "__main__":
    asyncio.run(main())
