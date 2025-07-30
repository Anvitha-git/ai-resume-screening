import React from 'react';
import './App.css';
import ResumeUpload from './components/ResumeUpload';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Resume Screening System</h1>
        <p>Job Seeker Dashboard</p>
        <ResumeUpload />
      </header>
    </div>
  );
}

export default App;