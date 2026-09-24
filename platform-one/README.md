# Platform-One - Orquestrador de Serviços

O **Platform-One** é um orquestrador completo que integra e gerencia os projetos **CNPJ-QA-Training** e **Fabrica-de-Testes** em um ambiente Docker unificado.

## 🏗️ Arquitetura

```
Platform-One (FastAPI + React)
├── CNPJ-QA-Training (Python/FastAPI) - Validação CNPJ
├── Fabrica-de-Testes (Node.js/React) - Plataforma de QA
├── PostgreSQL - Banco de dados
└── Redis - Cache e fila de mensagens
```

## 🚀 Funcionalidades

### Orquestração de Serviços
- **Monitoramento em Tempo Real**: Status e saúde de todos os serviços
- **Workflows Integrados**: Validação CNPJ → Testes Automatizados
- **APIs Unificadas**: Interface única para múltiplos serviços
- **Webhooks**: Notificações assíncronas de eventos

### Dashboard Interativo
- **Status Visual**: Cards com indicadores de saúde dos serviços
- **Monitor de Logs**: Atividades em tempo real
- **Execução de Testes**: Interface para rodar validações e testes
- **Métricas de Performance**: Latência, uptime, requests/minuto

## 📋 Pré-requisitos

- Docker Desktop 4.0+
- Docker Compose 2.0+
- 4GB RAM disponível
- 10GB espaço em disco

## 🛠️ Instalação e Execução

### 1. Clonagem dos Projetos
```bash
# Certifique-se de ter todos os projetos no mesmo diretório
ls -la
# Deve conter: CNPJ-QA-Training/, Fabrica-de-Testes/, Platform-One/
```

### 2. Configuração do Ambiente
```bash
cd platform-one
# O arquivo .env será criado automaticamente no primeiro startup
```

### 3. Inicialização dos Serviços
```bash
# Windows
scripts\start-all.bat

# Linux/Mac
./scripts/start-all.sh
```

### 4. Verificação da Instalação
```bash
# Health check
python scripts/health-check.py

# Ou via API
curl http://localhost:8001/health
```

## 🌐 Acesso aos Serviços

| Serviço | URL | Descrição |
|---------|-----|-----------|
| **Platform-One** | http://localhost:8001 | Dashboard do orquestrador |
| **CNPJ-QA-Training** | http://localhost:8000 | API de validação CNPJ |
| **Fabrica Backend** | http://localhost:3000 | Backend da plataforma QA |
| **Fabrica Frontend** | http://localhost:5173 | Interface da plataforma QA |

## 📚 APIs Disponíveis

### Platform-One APIs

#### Health Check
```bash
GET /health
# Retorna status geral do sistema
```

#### Status dos Serviços
```bash
GET /status
# Retorna status detalhado de todos os serviços
```

#### Validação CNPJ
```bash
POST /cnpj/validate
{
  "cnpj": "00.000.000/0001-91",
  "validate_receita": false
}
```

#### Execução de Testes
```bash
POST /tests/execute
{
  "test_type": "cnpj_validation",
  "parameters": {
    "cnpj": "00.000.000/0001-91"
  }
}
```

#### Registro de Webhooks
```bash
POST /webhooks/register
{
  "event_type": "cnpj_validation_completed",
  "webhook_url": "http://your-service.com/webhook"
}
```

## 🔧 Desenvolvimento

### Estrutura do Projeto
```
platform-one/
├── backend/                 # FastAPI backend
│   ├── main.py             # API principal
│   ├── orchestrator.py     # Lógica de orquestração
│   ├── proxy.py            # Comunicação com serviços
│   ├── models.py           # Modelos Pydantic
│   ├── config.py           # Configurações
│   ├── requirements.txt    # Dependências Python
│   └── Dockerfile
├── frontend/                # React frontend
│   ├── src/
│   │   ├── App.jsx         # Componente principal
│   │   ├── components/     # Componentes React
│   │   └── index.css       # Estilos Tailwind
│   ├── package.json
│   └── vite.config.js
├── config/                  # Configurações
│   ├── services.yaml       # Configuração dos serviços
│   └── init.sql           # Inicialização do banco
├── scripts/                 # Scripts utilitários
│   ├── health-check.py     # Verificação de saúde
│   └── start-all.bat       # Inicialização Windows
├── docker-compose.yml       # Orquestração Docker
└── .env.example            # Variáveis de ambiente
```

### Desenvolvimento Local

#### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

#### Frontend (React)
```bash
cd frontend
npm install
npm run dev
```

## 🧪 Testes

### Health Check Automático
```bash
python scripts/health-check.py --json
```

### Testes de Integração
```bash
# Via Dashboard: http://localhost:8001
# Ou via API
curl -X POST http://localhost:8001/tests/execute \
  -H "Content-Type: application/json" \
  -d '{"test_type": "cnpj_validation", "parameters": {"cnpj": "00.000.000/0001-91"}}'
```

## 📊 Monitoramento

### Logs em Tempo Real
```bash
# Todos os serviços
docker-compose logs -f

# Serviço específico
docker-compose logs -f platform-one
```

### Métricas de Performance
- **Dashboard**: http://localhost:8001 (aba Monitor)
- **Health API**: http://localhost:8001/health
- **Status API**: http://localhost:8001/status

## 🔄 Workflows

### Workflow de Validação CNPJ
1. **Recebimento**: CNPJ via API `/cnpj/validate`
2. **Validação Básica**: Verificação algoritmo CNPJ
3. **Validação Receita**: Consulta API Receita Federal (opcional)
4. **Execução de Testes**: Testes automatizados no Fabrica-de-Testes
5. **Notificação**: Webhooks para sistemas externos

### Workflow de Testes
1. **Recebimento**: Parâmetros via API `/tests/execute`
2. **Orquestração**: Coordenação entre serviços
3. **Execução**: Testes no Fabrica-de-Testes
4. **Resultados**: Agregação e retorno
5. **Notificação**: Webhooks com resultados

## 🚨 Troubleshooting

### Serviços Não Iniciam
```bash
# Verificar logs
docker-compose logs

# Reiniciar serviços
docker-compose restart

# Reconstruir e reiniciar
docker-compose up --build --force-recreate
```

### Problemas de Conectividade
```bash
# Verificar portas
netstat -tulpn | grep :800

# Testar conectividade
curl http://localhost:8001/health
```

### Limpeza do Ambiente
```bash
# Parar e remover tudo
docker-compose down -v --remove-orphans

# Limpar imagens não utilizadas
docker system prune -f
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Documentação**: [Docs](./docs/)
- **Wiki**: [Wiki do Projeto](https://github.com/your-repo/wiki)

---

**Desenvolvido com ❤️ para integração e orquestração de serviços de QA**
