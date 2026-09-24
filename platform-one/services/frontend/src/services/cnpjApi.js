import axios from 'axios';

// Usando proxy do package.json, então base vazia
const API_BASE = '';

export const cnpjApi = {
  // Validação básica
  validateBasic: async (cnpj) => {
    const response = await axios.get(`${API_BASE}/validate/basic/${cnpj}`);
    return response.data;
  },

  // Validação detalhada
  validateDetailed: async (cnpj) => {
    const response = await axios.get(`${API_BASE}/validate/detailed/${cnpj}`);
    return response.data;
  },

  // Consulta Receita Federal
  consultaReceita: async (cnpj) => {
    const response = await axios.get(`${API_BASE}/consulta/${cnpj}`);
    return response.data;
  },

  // Status da API
  healthCheck: async () => {
    const response = await axios.get(`${API_BASE}/status`);
    return response.data;
  },

  // Formatação
  formatCnpj: async (cnpj) => {
    const response = await axios.get(`${API_BASE}/format/${cnpj}`);
    return response.data;
  }
};
