import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [serviceStatus, setServiceStatus] = useState("");

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('http://localhost:8000/predict_gun', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setPrediction(response.data);
    } catch (error) {
      console.error('Error al realizar la predicción:', error);
    }
  };

  const checkServiceStatus = async () => {
    try {
      const response = await axios.get('http://localhost:8000/status');
      setServiceStatus(response.data.status);
    } catch (error) {
      console.error('Error al verificar el estado del servicio:', error);
    }
  };

  const downloadReport = async () => {
    try {
      const response = await axios.get('http://localhost:8000/reports', { responseType: 'blob' });
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'predictions_report.csv');
      document.body.appendChild(link);
      link.click();
    } catch (error) {
      console.error('Error al descargar el reporte:', error);
    }
  };

  return (
    <div className="App">
      <h1>Detector de Armas</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Subir y Predecir</button>
      {prediction && <div>Resultado de la Predicción: {JSON.stringify(prediction)}</div>}
      <button onClick={checkServiceStatus}>Verificar Estado del Servicio</button>
      {serviceStatus && <div>Estado del Servicio: {serviceStatus}</div>}
      <button onClick={downloadReport}>Descargar Reporte</button>
    </div>
  );
}

export default App;