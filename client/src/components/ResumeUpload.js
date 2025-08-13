import React, { useState } from 'react';
import axios from 'axios';

function ResumeUpload() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) {
      alert('Please select a file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      // Upload resume to backend
      const response = await axios.post('http://10.217.42.144:8000/upload_resume', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      console.log('Backend Response:', response.data);

      // Notify chatbot
      const chatbotResponse = await axios.post('http://localhost:5005/webhooks/rest/webhook', {
        sender: 'user',
        message: 'I uploaded my resume',
      });
      console.log('Chatbot Response:', chatbotResponse.data);

      alert('Resume uploaded successfully!');
    } catch (error) {
      console.error('Error:', error);
      alert('Failed to upload resume');
    }
  };

  return (
    <div>
      <h2>Upload Resume</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".pdf,.doc,.docx,.png,.jpg" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default ResumeUpload;