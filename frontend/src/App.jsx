import React, { useEffect, useState } from 'react';

function App() {
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Replace with your Flask server URL
    fetch('http://localhost:5000/status')
      .then((res) => res.json())
      .then(
        (result) => {
          setResponse(result.status);
        },
        (error) => {
          setError(error);
        }
      );
  }, []);

  return (
    <div className="App">
      <h1>Flask Response</h1>
      {error && <p>Error: {error.message}</p>}
      {response ? <p>{response}</p> : <p>Loading...</p>}
    </div>
  );
}

export default App;
