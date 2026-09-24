import React, { useState, useEffect, useRef } from 'react';

const AiAgentDashboard = () => {
  const [logs, setLogs] = useState([]);
  const [status, setStatus] = useState('Disconnected');
  const wsRef = useRef(null);
  const terminalRef = useRef(null);

  useEffect(() => {
    // Connect to the Platform-One proxy WebSocket for AI
    wsRef.current = new WebSocket('ws://localhost:8001/ai/ws');

    wsRef.current.onopen = () => {
      setStatus('Connected');
    };

    wsRef.current.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        setLogs((prev) => [...prev, data]);
      } catch (e) {
        // If not JSON, treat as raw text log
        setLogs((prev) => [...prev, { type: 'raw', message: event.data }]);
      }
    };

    wsRef.current.onclose = () => {
      setStatus('Disconnected');
    };

    return () => {
      if (wsRef.current) wsRef.current.close();
    };
  }, []);

  useEffect(() => {
    // Auto-scroll to bottom
    if (terminalRef.current) {
      terminalRef.current.scrollTop = terminalRef.current.scrollHeight;
    }
  }, [logs]);

  return (
    <div className="p-4 bg-gray-900 text-white min-h-[500px] rounded-lg shadow-xl font-mono text-sm">
      <div className="flex justify-between items-center mb-4 border-b border-gray-700 pb-2">
        <h2 className="text-xl font-bold text-blue-400">🧠 AI Agents Observability</h2>
        <span className={`px-2 py-1 rounded text-xs ${status === 'Connected' ? 'bg-green-600' : 'bg-red-600'}`}>
          {status}
        </span>
      </div>
      
      <div 
        ref={terminalRef}
        className="h-[400px] overflow-y-auto space-y-2 bg-black p-4 rounded border border-gray-800"
      >
        {logs.map((log, idx) => {
          if (log.type === 'log') {
            return <div key={idx} className="text-gray-300">{log.message}</div>;
          }
          if (log.type === 'thought') {
            return <div key={idx} className="text-purple-400">💭 {log.content}</div>;
          }
          if (log.type === 'code_chunk') {
            return <div key={idx} className="text-yellow-300">📝 [{log.file}]: {log.chunk}</div>;
          }
          if (log.type === 'terminal') {
            return <div key={idx} className={log.isError ? "text-red-500" : "text-green-400"}>
              {log.isError ? "❌" : "📟"} {log.output}
            </div>;
          }
          return <div key={idx} className="text-gray-500">{log.message || JSON.stringify(log)}</div>;
        })}
        {logs.length === 0 && <div className="text-gray-600 italic">Waiting for agent activity...</div>}
      </div>
    </div>
  );
};

export default AiAgentDashboard;
