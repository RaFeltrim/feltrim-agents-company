import React from 'react';
import { Card, CardContent, CardHeader, Typography, Chip, Divider } from '@mui/material';

const ValidacaoCard = ({ title, data }) => {
  const isValid = data?.valid === true;
  return (
    <Card>
      <CardHeader
        title={title}
        subheader={`CNPJ: ${data?.cnpjFormatado || data?.cnpj_formatted || 'N/A'}`}
        avatar={
          <Chip 
            label={isValid ? 'VÁLIDO' : 'INVÁLIDO'} 
            color={isValid ? 'success' : 'error'}
            variant="filled"
          />
        }
      />
      <CardContent>
        <Typography variant="body2">
          <strong>Status:</strong> {data?.status || 'N/A'}
        </Typography>
        {data?.message && (
          <>
            <Divider sx={{ my: 1 }} />
            <Typography variant="body2" color="text.secondary">
              {data.message}
            </Typography>
          </>
        )}
        {data?.details && (
          <>
            <Divider sx={{ my: 1 }} />
            <Typography variant="body2"><strong>Detalhes:</strong></Typography>
            <pre style={{ fontSize: '0.8rem', overflow: 'auto' }}>
              {JSON.stringify(data.details, null, 2)}
            </pre>
          </>
        )}
      </CardContent>
    </Card>
  );
};

export default ValidacaoCard;
