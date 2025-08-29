import React, { useState } from "react";
import { analyzeData } from "./api";

function App() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState([]);

  const handleUpload = async () => {
    if (!file) return;
    const res = await analyzeData(file);
    setResults(res.data.predictions);
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">AI Healthcare Tool</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload & Analyze</button>
      <div>
        <h2>Results:</h2>
        <ul>
          {results.map((r, i) => (
            <li key={i}>Prediction {i + 1}: {r}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
