import React, { useState } from 'react';
import axios from 'axios';
import './ATS.css';

const ATS = () => {
  const [jd, setJd] = useState('');
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('jd', jd);
    formData.append('file', file);

    try {
      const res = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResponse(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="ats-container">
      <h1>Smart ATS</h1>
      <p>Improve Your Resume ATS</p>
      <form className="ats-form" onSubmit={handleSubmit}>
        <textarea
          className="ats-textarea"
          placeholder="Paste the Job Description"
          value={jd}
          onChange={(e) => setJd(e.target.value)}
        />
        <input
          className="ats-file-input"
          type="file"
          accept="application/pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button className="ats-submit-button" type="submit">Submit</button>
      </form>
      {response && (
        <div className="ats-response">
          <h2>Response:</h2>
          <pre>{response}</pre>
        </div>
      )}
    </div>
  );
};

export default ATS;
