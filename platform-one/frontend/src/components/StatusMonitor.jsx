import React, { useState, useEffect } from 'react';
import { Activity, Server, Database, Zap, Code, Globe } from 'lucide-react';

function StatusMonitor() {
  const [logs, setLogs] = useState([]);
  const [filter, setFilter] = useState('all');

  // Simulação de logs - em produção, conectar com API de logs
  useEffect(() => {
    const mockLogs = [
      {
        id: 1,
        timestamp: new Date(Date.now() - 1000 * 60 * 5).toISOString(),
        service: 'platform-one',
        level: 'info',
        message: 'Orquestrador iniciado com sucesso',
        icon: Server
      },
      {
        id: 2,
        timestamp: new Date(Date.now() - 1000 * 60 * 4).toISOString(),
        service: 'cnpj-qa-training',
        level: 'info',
        message: 'API CNPJ validada e conectada',
        icon: Code
      },
      {
        id: 3,
        timestamp: new Date(Date.now() - 1000 * 60 * 3).toISOString(),
        service: 'postgres',
        level: 'info',
        message: 'Conexão com banco de dados estabelecida',
        icon: Database
      },
      {
        id: 4,
        timestamp: new Date(Date.now() - 1000 * 60 * 2).toISOString(),
        service: 'redis',
        level: 'info',
        message: 'Cache Redis inicializado',
        icon: Zap
      },
      {
        id: 5,
        timestamp: new Date(Date.now() - 1000 * 60 * 1).toISOString(),
        service: 'fabrica-backend',
        level: 'warning',
        message: 'Verificação de saúde lenta (2.1s)',
        icon: Globe
      }
    ];

    setLogs(mockLogs);
  }, []);

  const getLevelColor = (level) => {
    switch (level) {
      case 'error':
        return 'text-red-600 bg-red-50';
      case 'warning':
        return 'text-yellow-600 bg-yellow-50';
      case 'info':
        return 'text-blue-600 bg-blue-50';
      default:
        return 'text-gray-600 bg-gray-50';
    }
  };

  const filteredLogs = logs.filter(log =>
    filter === 'all' || log.service === filter
  );

  const services = [
    { id: 'all', name: 'Todos os Serviços', icon: Activity },
    { id: 'platform-one', name: 'Platform-One', icon: Server },
    { id: 'cnpj-qa-training', name: 'CNPJ-QA-Training', icon: Code },
    { id: 'postgres', name: 'PostgreSQL', icon: Database },
    { id: 'redis', name: 'Redis', icon: Zap },
    { id: 'fabrica-backend', name: 'Fabrica Backend', icon: Globe },
    { id: 'fabrica-frontend', name: 'Fabrica Frontend', icon: Globe }
  ];

  return (
    <div className="space-y-6">
      {/* Service Filter */}
      <div className="card">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">Monitor de Atividades</h2>

        <div className="flex flex-wrap gap-2">
          {services.map((service) => {
            const Icon = service.icon;
            return (
              <button
                key={service.id}
                onClick={() => setFilter(service.id)}
                className={`flex items-center px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                  filter === service.id
                    ? 'bg-primary-100 text-primary-800 border-primary-300'
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200 border-gray-300'
                } border`}
              >
                <Icon className="w-4 h-4 mr-2" />
                {service.name}
              </button>
            );
          })}
        </div>
      </div>

      {/* Logs */}
      <div className="card">
        <div className="flex justify-between items-center mb-4">
          <h3 className="text-lg font-semibold text-gray-900">Logs de Atividade</h3>
          <span className="text-sm text-gray-500">
            {filteredLogs.length} entradas
          </span>
        </div>

        <div className="space-y-3 max-h-96 overflow-y-auto">
          {filteredLogs.map((log) => {
            const Icon = log.icon;
            return (
              <div
                key={log.id}
                className="flex items-start space-x-3 p-3 rounded-lg border border-gray-200 hover:bg-gray-50"
              >
                <div className={`p-2 rounded-full ${getLevelColor(log.level)}`}>
                  <Icon className="w-4 h-4" />
                </div>

                <div className="flex-1 min-w-0">
                  <div className="flex items-center justify-between">
                    <p className="text-sm font-medium text-gray-900">
                      {log.service}
                    </p>
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${getLevelColor(log.level)}`}>
                      {log.level.toUpperCase()}
                    </span>
                  </div>

                  <p className="text-sm text-gray-600 mt-1">
                    {log.message}
                  </p>

                  <p className="text-xs text-gray-400 mt-1">
                    {new Date(log.timestamp).toLocaleString('pt-BR')}
                  </p>
                </div>
              </div>
            );
          })}
        </div>

        {filteredLogs.length === 0 && (
          <div className="text-center py-8">
            <Activity className="w-12 h-12 text-gray-400 mx-auto mb-4" />
            <p className="text-gray-600">Nenhum log encontrado para o filtro selecionado.</p>
          </div>
        )}
      </div>

      {/* System Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="card">
          <h4 className="text-sm font-medium text-gray-500 mb-2">Uptime do Sistema</h4>
          <p className="text-2xl font-bold text-gray-900">99.9%</p>
          <p className="text-sm text-gray-600">Últimas 24 horas</p>
        </div>

        <div className="card">
          <h4 className="text-sm font-medium text-gray-500 mb-2">Requests por Minuto</h4>
          <p className="text-2xl font-bold text-gray-900">1,247</p>
          <p className="text-sm text-gray-600">Média atual</p>
        </div>

        <div className="card">
          <h4 className="text-sm font-medium text-gray-500 mb-2">Latência Média</h4>
          <p className="text-2xl font-bold text-gray-900">45ms</p>
          <p className="text-sm text-gray-600">Últimos 5 minutos</p>
        </div>
      </div>
    </div>
  );
}

export default StatusMonitor;