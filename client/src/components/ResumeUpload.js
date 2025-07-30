import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';

function ResumeUpload() {
  const [uploadedFile, setUploadedFile] = useState(null);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: {
      'application/pdf': ['.pdf'],
      'application/msword': ['.doc'],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
      'image/png': ['.png'],
      'image/jpeg': ['.jpg', '.jpeg']
    },
    onDrop: (acceptedFiles) => {
      console.log('Uploaded files:', acceptedFiles);
      if (acceptedFiles.length > 0) {
        setUploadedFile(acceptedFiles[0]); // Store the first file
      }
    }
  });

  return (
    <div {...getRootProps()} className="upload-container">
      <input {...getInputProps()} />
      {isDragActive ? (
        <p>Drop your resume here...</p>
      ) : (
        <p>Drag and drop your resume (PDF, DOC, PNG, JPG) or click to select</p>
      )}
      {uploadedFile && (
        <p style={{ color: 'lightgreen', marginTop: '10px' }}>
          Uploaded: {uploadedFile.name}
        </p>
      )}
    </div>
  );
}

export default ResumeUpload;