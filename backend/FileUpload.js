import React, { useState } from 'react';
import axios from 'axios';

function FileUpload() {
  const [file, setFile] = useState(null);
  const [progress, setProgress] = useState(0);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = () => {
    const formData = new FormData();
    formData.append('file', file);

    axios.post('http://127.0.0.1:5000/upload', formData, { // Ensure this URL is correct
      onUploadProgress: (progressEvent) => {
        const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
        setProgress(percentCompleted);
      }
    })
    .then(response => {
      console.log('File uploaded successfully');
    })
    .catch(error => {
      console.error('Error uploading file:', error);
    });
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      {progress > 0 && <div>Progress: {progress}%</div>}
    </div>
  );
}

export default FileUpload;

