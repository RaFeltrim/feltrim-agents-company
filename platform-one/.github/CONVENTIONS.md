# Convenções Platform One

## Microsserviços
- Portas: api-gateway (3000), test-hub-ms (5050), fabrica-ms (3001)
- Logs: JSON estruturado
- Health checks: GET /health
- Status codes: RESTful padrão

## Variáveis de Ambiente
- DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
- SERVICE_TEST_HUB_URL
- SERVICE_FABRICA_URL
- JWT_SECRET (para auth futura)

## Commits
- Formato: [SERVICE] Message (ex: [api-gateway] Add user auth)
- Branching: feature/service-name, bugfix/issue-number

## Database
- PostgreSQL 14+
- Migrations: Alembic (Python) ou Flyway
- Schemas separados por serviço
