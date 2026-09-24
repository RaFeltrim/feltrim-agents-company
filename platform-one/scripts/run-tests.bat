@echo off
REM Script para rodar todos os testes Python do monorepo
REM Garante que o PYTHONPATH inclui a pasta src
setlocal
set PYTHONPATH=src
"C:/Users/RafaelFeltrim/Desktop/Projetos/CNPJ-QA-Training/.venv/Scripts/python.exe" -m pytest tests/
endlocal
