import React, { useState, useEffect } from 'react';
import Dashboard from './components/Dashboard';
import StatusMonitor from './components/StatusMonitor';
import AiAgentDashboard from './components/AiAgentDashboard';
import TestModal from './components/TestModal';
import { Activity, Settings, TestTube, Brain } from 'lucide-react';

function App() {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [showTestModal, setShowTestModal] = useState(false);
  const [systemStatus, setSystemStatus] = useState(null);

  useEffect(() => {
    // Verificar status do sistema periodicamente
    const checkStatus = async () => {
      try {
        const response = await fetch('/api/health');
        const data = await response.json();
        setSystemStatus(data);
      } catch (error) {
        console.error('Erro ao verificar status:', error);
      }
    };

    checkStatus();
    const interval = setInterval(checkStatus, 30000); // A cada 30 segundos

    return () => clearInterval(interval);
  }, []);

  const tabs = [
    { id: 'dashboard', label: 'Dashboard', icon: Activity },
    { id: 'monitor', label: 'Monitor', icon: Settings },
    { id: 'ai-agents', label: 'AI Agents', icon: Brain },
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center">
              <h1 className="text-2xl font-bold text-gray-900">Platform-One</h1>
              <span className="ml-2 text-sm text-gray-500">Orquestrador</span>
            </div>

            <div className="flex items-center space-x-4">
              {/* Status Indicator */}
              <div className="flex items-center">
                <div className={`status-indicator ${
                  systemStatus?.status === 'healthy' ? 'status-healthy' :
                  systemStatus?.status === 'degraded' ? 'status-warning' : 'status-error'
                }`}></div>
                <span className="text-sm text-gray-600">
                  {systemStatus?.status === 'healthy' ? 'Sistema Saudável' :
                   systemStatus?.status === 'degraded' ? 'Sistema Degradado' : 'Sistema Indisponível'}
                </span>
              </div>

              {/* Test Button */}
              <button
                onClick={() => setShowTestModal(true)}
                className="btn btn-primary flex items-center"
              >
                <TestTube className="w-4 h-4 mr-2" />
                Executar Teste
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Navigation */}
      <nav className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex space-x-8">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`flex items-center px-1 py-4 border-b-2 font-medium text-sm ${
                    activeTab === tab.id
                      ? 'border-primary-500 text-primary-600'
                      : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                  }`}
                >
                  <Icon className="w-4 h-4 mr-2" />
                  {tab.label}
                </button>
              );
            })}
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        {activeTab === 'dashboard' && <Dashboard />}
        {activeTab === 'monitor' && <StatusMonitor />}
        {activeTab === 'ai-agents' && <AiAgentDashboard />}
      </main>

      {/* Test Modal */}
      {showTestModal && (
        <TestModal onClose={() => setShowTestModal(false)} />
      )}
    </div>
  );
}

export default App;