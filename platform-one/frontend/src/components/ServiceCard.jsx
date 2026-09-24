import React from 'react';
import { ExternalLink, Clock, Zap } from 'lucide-react';

function ServiceCard({ service }) {
  const getStatusColor = (status) => {
    switch (status) {
      case 'healthy':
      case 'running':
        return 'bg-success-100 text-success-800 border-success-200';
      case 'unhealthy':
        return 'bg-warning-100 text-warning-800 border-warning-200';
      case 'error':
        return 'bg-error-100 text-error-800 border-error-200';
      default:
        return 'bg-gray-100 text-gray-800 border-gray-200';
    }
  };

  const getStatusIcon = (status) => {
    switch (status) {
      case 'healthy':
      case 'running':
        return '🟢';
      case 'unhealthy':
        return '🟡';
      case 'error':
        return '🔴';
      default:
        return '⚪';
    }
  };

  const formatResponseTime = (time) => {
    if (!time) return 'N/A';
    return `${(time * 1000).toFixed(0)}ms`;
  };

  const formatLastCheck = (timestamp) => {
    if (!timestamp) return 'Nunca';
    return new Date(timestamp).toLocaleString('pt-BR');
  };

  return (
    <div className="card hover:shadow-lg transition-shadow duration-200">
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <h3 className="text-lg font-semibold text-gray-900 mb-1">
            {service.name}
          </h3>
          <div className="flex items-center space-x-2">
            <span className={`px-2 py-1 rounded-full text-xs font-medium border ${getStatusColor(service.status)}`}>
              {getStatusIcon(service.status)} {service.status}
            </span>
          </div>
        </div>
        <a
          href={service.url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-gray-400 hover:text-gray-600 transition-colors"
        >
          <ExternalLink className="w-4 h-4" />
        </a>
      </div>

      <div className="space-y-2 text-sm text-gray-600">
        <div className="flex items-center">
          <Clock className="w-4 h-4 mr-2 text-gray-400" />
          <span>Última verificação: {formatLastCheck(service.lastCheck)}</span>
        </div>

        {service.responseTime && (
          <div className="flex items-center">
            <Zap className="w-4 h-4 mr-2 text-gray-400" />
            <span>Tempo de resposta: {formatResponseTime(service.responseTime)}</span>
          </div>
        )}

        <div className="pt-2">
          <a
            href={service.url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-primary-600 hover:text-primary-800 text-sm font-medium"
          >
            Acessar serviço →
          </a>
        </div>
      </div>
    </div>
  );
}

export default ServiceCard;