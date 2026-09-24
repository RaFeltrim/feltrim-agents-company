-- Schema Test Hub
CREATE SCHEMA test_hub;

CREATE TABLE test_hub.projects (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    test_types TEXT[] DEFAULT ARRAY['pytest'],
    config JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE test_hub.executions (
    id UUID PRIMARY KEY,
    project_id UUID NOT NULL REFERENCES test_hub.projects(id),
    status VARCHAR(50) DEFAULT 'pending',
    started_at TIMESTAMP,
    ended_at TIMESTAMP,
    duration_ms INTEGER,
    results JSONB,
    artifacts JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE test_hub.test_results (
    id UUID PRIMARY KEY,
    execution_id UUID NOT NULL REFERENCES test_hub.executions(id),
    test_name VARCHAR(255),
    status VARCHAR(50),
    duration_ms INTEGER,
    error_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Schema Fabrica (E2E)
CREATE SCHEMA fabrica;

CREATE TABLE fabrica.test_suites (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    framework VARCHAR(50),
    config JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE fabrica.e2e_executions (
    id UUID PRIMARY KEY,
    suite_id UUID NOT NULL REFERENCES fabrica.test_suites(id),
    status VARCHAR(50) DEFAULT 'pending',
    started_at TIMESTAMP,
    ended_at TIMESTAMP,
    duration_ms INTEGER,
    results JSONB,
    videos JSONB,
    screenshots JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Schema Analytics (Compartilhado)
CREATE SCHEMA analytics;

CREATE TABLE analytics.execution_history (
    id UUID PRIMARY KEY,
    service VARCHAR(50),
    execution_id UUID NOT NULL,
    total_tests INTEGER,
    passed INTEGER,
    failed INTEGER,
    skipped INTEGER,
    success_rate DECIMAL(5,2),
    duration_ms INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE analytics.trends (
    id UUID PRIMARY KEY,
    service VARCHAR(50),
    date DATE,
    total_tests INTEGER,
    success_rate DECIMAL(5,2),
    avg_duration_ms INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para Performance
CREATE INDEX idx_executions_project ON test_hub.executions(project_id);
CREATE INDEX idx_executions_status ON test_hub.executions(status);
CREATE INDEX idx_executions_created ON test_hub.executions(created_at);
CREATE INDEX idx_e2e_executions_suite ON fabrica.e2e_executions(suite_id);
CREATE INDEX idx_history_timestamp ON analytics.execution_history(timestamp);
CREATE INDEX idx_trends_date ON analytics.trends(date);
