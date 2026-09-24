-- Platform-One Database Initialization

-- Create database if it doesn't exist
-- (This is handled by docker-compose environment variables)

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create schemas
CREATE SCHEMA IF NOT EXISTS platform_one;

-- Service status tracking table
CREATE TABLE IF NOT EXISTS platform_one.service_status (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    service_name VARCHAR(100) UNIQUE NOT NULL,
    status VARCHAR(50) NOT NULL,
    last_check TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    response_time FLOAT,
    error_message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Webhook events table
CREATE TABLE IF NOT EXISTS platform_one.webhook_events (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_type VARCHAR(100) NOT NULL,
    service VARCHAR(100) NOT NULL,
    data JSONB,
    processed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Test executions table
CREATE TABLE IF NOT EXISTS platform_one.test_executions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    execution_id VARCHAR(100) UNIQUE NOT NULL,
    test_type VARCHAR(100) NOT NULL,
    parameters JSONB,
    status VARCHAR(50) NOT NULL,
    results JSONB,
    error_message TEXT,
    started_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    completed_at TIMESTAMP WITH TIME ZONE
);

-- CNPJ validations table
CREATE TABLE IF NOT EXISTS platform_one.cnpj_validations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    cnpj VARCHAR(18) NOT NULL,
    is_valid BOOLEAN NOT NULL,
    formatted_cnpj VARCHAR(18),
    receita_data JSONB,
    validation_type VARCHAR(50) DEFAULT 'basic',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_service_status_name ON platform_one.service_status(service_name);
CREATE INDEX IF NOT EXISTS idx_service_status_last_check ON platform_one.service_status(last_check);
CREATE INDEX IF NOT EXISTS idx_webhook_events_type ON platform_one.webhook_events(event_type);
CREATE INDEX IF NOT EXISTS idx_webhook_events_processed ON platform_one.webhook_events(processed);
CREATE INDEX IF NOT EXISTS idx_test_executions_status ON platform_one.test_executions(status);
CREATE INDEX IF NOT EXISTS idx_cnpj_validations_cnpj ON platform_one.cnpj_validations(cnpj);

-- Insert initial service records
INSERT INTO platform_one.service_status (service_name, status) VALUES
    ('platform-one', 'running'),
    ('postgres', 'healthy'),
    ('redis', 'healthy'),
    ('cnpj-qa-training', 'unknown'),
    ('fabrica-backend', 'unknown'),
    ('fabrica-frontend', 'unknown')
ON CONFLICT (service_name) DO NOTHING;