import React, { useState, useEffect } from 'react';
import ServiceCard from './ServiceCard';
import { RefreshCw, CheckCircle, AlertTriangle, XCircle } from 'lucide-react';

function Dashboard() {
  const [services, setServices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [lastUpdate, setLastUpdate] = useState(null);

  const fetchServices = async () => {
    try {
      setLoading(true);
      const response = await fetch('/api/status');
      const data = await response.json();

      const serviceList = [
        {
          name: 'Platform-One',
          status: data.platform_one.status,
          url: data.platform_one.url,
          lastCheck: data.platform_one.last_check,
          responseTime: data.platform_one.response_time
        },
        {
          name: 'PostgreSQL',
          status: data.postgres.status,
          url: data.postgres.url,
          lastCheck: data.postgres.last_check,
          responseTime: data.postgres.response_time
        },
        {
          name: 'Redis',
          status: data.redis.status,
          url: data.redis.url,
          lastCheck: data.redis.last_check,
          responseTime: data.redis.response_time
        },
        {
          name: 'CNPJ-QA-Training',
          status: data.cnpj_qa_training.status,
          url: data.cnpj_qa_training.url,
          lastCheck: data.cnpj_qa_training.last_check,
          responseTime: data.cnpj_qa_training.response_time
        },
        {
          name: 'Fabrica Backend',
          status: data.fabrica_backend.status,
          url: data.fabrica_backend.url,
          lastCheck: data.fabrica_backend.last_check,
          responseTime: data.fabrica_backend.response_time
        },
        {
          name: 'Fabrica Frontend',
          status: data.fabrica_frontend.status,
          url: data.fabrica_frontend.url,
          lastCheck: data.fabrica_frontend.last_check,
          responseTime: data.fabrica_frontend.response_time
        }
      ];

      setServices(serviceList);
      setLastUpdate(new Date().toLocaleString('pt-BR'));
    } catch (error) {
      console.error('Erro ao buscar status dos serviços:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchServices();
    const interval = setInterval(fetchServices, 30000); // Atualizar a cada 30 segundos
    return () => clearInterval(interval);
  }, []);

  const getStatusSummary = () => {
    const healthy = services.filter(s => s.status === 'healthy' || s.status === 'running').length;
    const unhealthy = services.filter(s => s.status === 'unhealthy').length;
    const error = services.filter(s => s.status === 'error').length;

    return { healthy, unhealthy, error, total: services.length };
  };

  const summary = getStatusSummary();

  return (
    <div className="space-y-6">
      {/* Status Summary */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="card">
          <div className="flex items-center">
            <CheckCircle className="w-8 h-8 text-success-500 mr-3" />
            <div>
              <p className="text-2xl font-bold text-success-600">{summary.healthy}</p>
              <p className="text-sm text-gray-600">Saudáveis</p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <AlertTriangle className="w-8 h-8 text-warning-500 mr-3" />
            <div>
              <p className="text-2xl font-bold text-warning-600">{summary.unhealthy}</p>
              <p className="text-sm text-gray-600">Degradados</p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <XCircle className="w-8 h-8 text-error-500 mr-3" />
            <div>
              <p className="text-2xl font-bold text-error-600">{summary.error}</p>
              <p className="text-sm text-gray-600">Com Erro</p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <RefreshCw className="w-8 h-8 text-primary-500 mr-3" />
            <div>
              <p className="text-2xl font-bold text-primary-600">{summary.total}</p>
              <p className="text-sm text-gray-600">Total</p>
            </div>
          </div>
        </div>
      </div>

      {/* Services Grid */}
      <div className="card">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-xl font-semibold text-gray-900">Status dos Serviços</h2>
          <div className="flex items-center space-x-4">
            {lastUpdate && (
              <span className="text-sm text-gray-500">
                Última atualização: {lastUpdate}
              </span>
            )}
            <button
              onClick={fetchServices}
              disabled={loading}
              className="btn btn-secondary flex items-center"
            >
              <RefreshCw className={`w-4 h-4 mr-2 ${loading ? 'animate-spin' : ''}`} />
              Atualizar
            </button>
          </div>
        </div>

        {loading && services.length === 0 ? (
          <div className="text-center py-8">
            <RefreshCw className="w-8 h-8 animate-spin mx-auto text-gray-400 mb-4" />
            <p className="text-gray-600">Carregando status dos serviços...</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {services.map((service) => (
              <ServiceCard key={service.name} service={service} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Dashboard;