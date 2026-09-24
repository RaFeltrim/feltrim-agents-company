import React, { useState, useEffect } from 'react';
import { cnpjApi } from '../services/cnpjApi';
import { TextField, Button, Card, CardContent, Typography, Box, Grid } from '@mui/material';
import ValidacaoCard from '../components/ValidacaoCard';

const Dashboard = () => {
  const [cnpj, setCnpj] = useState('');
  const [resultados, setResultados] = useState({});
  const [statusApi, setStatusApi] = useState('Verificando...');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    checkApiStatus();
  }, []);

  const checkApiStatus = async () => {
    try {
      const status = await cnpjApi.healthCheck();
      if (status.status === 'ok') {
        setStatusApi(status.message || 'API OK');
      } else {
        setStatusApi('API com problema');
      }
    } catch (error) {
      setStatusApi('API Offline');
    }
  };

  const validarCnpj = async () => {
    if (!cnpj) return;
    setLoading(true);
    try {
      const [basic, detailed] = await Promise.all([
        cnpjApi.validateBasic(cnpj),
        cnpjApi.validateDetailed(cnpj)
      ]);
      setResultados({ basic, detailed });
    } catch (error) {
      console.error('Erro na validação:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>
        Platform One - Hub CNPJ
      </Typography>
      <Card sx={{ mb: 3 }}>
        <CardContent>
          <Typography variant="h6">Status da API</Typography>
          <Typography color={statusApi.includes('OK') || statusApi.includes('rodando') ? 'success.main' : 'error'}>
            {statusApi}
          </Typography>
        </CardContent>
      </Card>
      <Grid container spacing={2}>
        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            label="Digite o CNPJ"
            value={cnpj}
            onChange={(e) => setCnpj(e.target.value.replace(/\D/g, ''))}
            placeholder="11222333000181"
          />
        </Grid>
        <Grid item xs={12} md={6}>
          <Button 
            variant="contained" 
            onClick={validarCnpj}
            disabled={loading || !cnpj}
            fullWidth
            sx={{ height: '100%' }}
          >
            {loading ? 'Validando...' : 'Validar CNPJ'}
          </Button>
        </Grid>
      </Grid>
      {resultados.basic && (
        <Grid container spacing={3} sx={{ mt: 2 }}>
          <Grid item xs={12} md={6}>
            <ValidacaoCard 
              title="Validação Básica" 
              data={resultados.basic} 
            />
          </Grid>
          <Grid item xs={12} md={6}>
            <ValidacaoCard 
              title="Validação Detalhada" 
              data={resultados.detailed} 
            />
          </Grid>
        </Grid>
      )}
    </Box>
  );
};

export default Dashboard;
