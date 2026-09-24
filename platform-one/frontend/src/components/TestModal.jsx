import React, { useState } from 'react';
import { X, Play, CheckCircle, AlertCircle, Loader } from 'lucide-react';

function TestModal({ onClose }) {
  const [testType, setTestType] = useState('cnpj_validation');
  const [cnpj, setCnpj] = useState('');
  const [validateReceita, setValidateReceita] = useState(false);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const testTypes = [
    {
      id: 'cnpj_validation',
      name: 'Validação CNPJ',
      description: 'Executa validação completa de CNPJ com testes integrados'
    },
    {
      id: 'api_integration',
      name: 'Integração API',
      description: 'Testa integração entre todos os serviços'
    },
    {
      id: 'performance',
      name: 'Performance',
      description: 'Executa testes de carga e performance'
    }
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    setError(null);

    try {
      let payload = { test_type: testType };

      if (testType === 'cnpj_validation') {
        payload.parameters = {
          cnpj: cnpj,
          validate_receita: validateReceita
        };
      }

      const response = await fetch('/api/tests/execute', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(`Erro na execução: ${response.status}`);
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const formatCNPJ = (value) => {
    // Remove tudo que não é dígito
    const digits = value.replace(/\D/g, '');

    // Aplica a máscara
    if (digits.length <= 2) return digits;
    if (digits.length <= 5) return `${digits.slice(0, 2)}.${digits.slice(2)}`;
    if (digits.length <= 8) return `${digits.slice(0, 2)}.${digits.slice(2, 5)}.${digits.slice(5)}`;
    if (digits.length <= 12) return `${digits.slice(0, 2)}.${digits.slice(2, 5)}.${digits.slice(5, 8)}/${digits.slice(8)}`;
    return `${digits.slice(0, 2)}.${digits.slice(2, 5)}.${digits.slice(5, 8)}/${digits.slice(8, 12)}-${digits.slice(12, 14)}`;
  };

  const handleCNPJChange = (e) => {
    const formatted = formatCNPJ(e.target.value);
    setCnpj(formatted);
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-xl max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        <div className="flex items-center justify-between p-6 border-b border-gray-200">
          <h2 className="text-xl font-semibold text-gray-900">Executar Teste</h2>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 transition-colors"
          >
            <X className="w-6 h-6" />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-6">
          {/* Test Type Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-3">
              Tipo de Teste
            </label>
            <div className="space-y-2">
              {testTypes.map((type) => (
                <label key={type.id} className="flex items-start">
                  <input
                    type="radio"
                    name="testType"
                    value={type.id}
                    checked={testType === type.id}
                    onChange={(e) => setTestType(e.target.value)}
                    className="mt-1 text-primary-600 focus:ring-primary-500"
                  />
                  <div className="ml-3">
                    <span className="text-sm font-medium text-gray-900">{type.name}</span>
                    <p className="text-sm text-gray-600">{type.description}</p>
                  </div>
                </label>
              ))}
            </div>
          </div>

          {/* CNPJ Input (only for CNPJ validation) */}
          {testType === 'cnpj_validation' && (
            <div className="space-y-4">
              <div>
                <label htmlFor="cnpj" className="block text-sm font-medium text-gray-700 mb-2">
                  CNPJ para Validação
                </label>
                <input
                  type="text"
                  id="cnpj"
                  value={cnpj}
                  onChange={handleCNPJChange}
                  placeholder="00.000.000/0000-00"
                  maxLength={18}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                  required
                />
              </div>

              <div className="flex items-center">
                <input
                  type="checkbox"
                  id="validateReceita"
                  checked={validateReceita}
                  onChange={(e) => setValidateReceita(e.target.checked)}
                  className="text-primary-600 focus:ring-primary-500"
                />
                <label htmlFor="validateReceita" className="ml-2 text-sm text-gray-700">
                  Validar com Receita Federal (mais lento, mas mais preciso)
                </label>
              </div>
            </div>
          )}

          {/* Submit Button */}
          <div className="flex justify-end space-x-3">
            <button
              type="button"
              onClick={onClose}
              className="btn btn-secondary"
            >
              Cancelar
            </button>
            <button
              type="submit"
              disabled={loading}
              className="btn btn-primary flex items-center"
            >
              {loading ? (
                <Loader className="w-4 h-4 mr-2 animate-spin" />
              ) : (
                <Play className="w-4 h-4 mr-2" />
              )}
              {loading ? 'Executando...' : 'Executar Teste'}
            </button>
          </div>
        </form>

        {/* Results */}
        {(result || error) && (
          <div className="px-6 pb-6">
            <div className="border-t border-gray-200 pt-6">
              <h3 className="text-lg font-medium text-gray-900 mb-4">Resultado</h3>

              {error && (
                <div className="bg-error-50 border border-error-200 rounded-md p-4">
                  <div className="flex items-center">
                    <AlertCircle className="w-5 h-5 text-error-600 mr-2" />
                    <span className="text-error-800 font-medium">Erro na execução</span>
                  </div>
                  <p className="text-error-700 mt-2">{error}</p>
                </div>
              )}

              {result && (
                <div className="bg-success-50 border border-success-200 rounded-md p-4">
                  <div className="flex items-center mb-3">
                    <CheckCircle className="w-5 h-5 text-success-600 mr-2" />
                    <span className="text-success-800 font-medium">Teste executado com sucesso</span>
                  </div>

                  <div className="space-y-2 text-sm">
                    <div><strong>ID da Execução:</strong> {result.execution_id}</div>
                    <div><strong>Status:</strong> {result.status}</div>
                    {result.results && (
                      <div>
                        <strong>Resultados:</strong>
                        <pre className="mt-1 bg-white p-2 rounded border text-xs overflow-x-auto">
                          {JSON.stringify(result.results, null, 2)}
                        </pre>
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default TestModal;