import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Container } from '@mui/material';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <Router>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Platform One
          </Typography>
          <Link to="/" style={{ color: 'white', textDecoration: 'none', marginRight: 16 }}>
            Dashboard
          </Link>
          <a href="http://127.0.0.1:8000/docs" style={{ color: 'white', textDecoration: 'none' }}>
            API Docs
          </a>
        </Toolbar>
      </AppBar>
      <Container maxWidth="lg">
        <Routes>
          <Route path="/" element={<Dashboard />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;
