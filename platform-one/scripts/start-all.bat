@echo off
REM Platform-One Start All Services Script
REM Inicia todos os serviços do sistema de orquestração

echo 🚀 Starting Platform-One Orchestration System
echo ==============================================

REM Verificar se Docker está instalado e rodando
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker não está instalado ou não está rodando.
    echo Por favor, instale o Docker Desktop e tente novamente.
    pause
    exit /b 1
)

REM Verificar se docker-compose está disponível
docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker Compose não está disponível.
    pause
    exit /b 1
)

REM Navegar para o diretório do projeto
cd /d "%~dp0.."

REM Criar arquivo .env se não existir
if not exist .env (
    echo 📋 Criando arquivo .env a partir do template...
    copy .env.example .env
    echo ✅ Arquivo .env criado. Você pode editá-lo se necessário.
)

REM Construir e iniciar todos os serviços
echo 🏗️  Construindo e iniciando serviços...
docker-compose up --build -d

REM Aguardar inicialização
echo ⏳ Aguardando inicialização dos serviços...
timeout /t 10 /nobreak >nul

REM Verificar saúde dos serviços
echo 🔍 Verificando saúde dos serviços...
python scripts\health-check.py

echo.
echo ✅ Sistema Platform-One iniciado!
echo.
echo 📊 Serviços disponíveis:
echo    • Platform-One Orchestrator: http://localhost:8001
echo    • CNPJ-QA-Training API:    http://localhost:8000
echo    • Fabrica Backend:         http://localhost:3000
echo    • Fabrica Frontend:        http://localhost:5173
echo.
echo 🛑 Para parar todos os serviços: docker-compose down
echo 📋 Para ver logs: docker-compose logs -f [service-name]
echo 🔍 Para health check: python scripts\health-check.py

pause