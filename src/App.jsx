import React, { useState } from 'react';
import './App.css';
import './index.css';
function App() {
  const [n, setN] = useState('');
  const [solutions, setSolutions] = useState([]);

  const solveNQueens = async () => {
    try {
      const response = await fetch('http://localhost:5000/solve_n_queens', 
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ n: parseInt(n) }),
      }
      );

      const data = await response.json();
      setSolutions(data.solutions);
    } 
    catch (error) 
    {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <div className="gif">
        <img src="https://lordicon.com/icons/wired/lineal/1481-chess-queen.gif" alt="Left GIF" />
      </div>
      <h1>N-Queens Problem Solver</h1>
      <label className="NEnter">
        Enter the side of the chessboard (N):
        <input
          type="number"
          value={n}
          onChange={(e) => setN(e.target.value)}
        />
      </label>
      <button onClick={solveNQueens}>Solve</button>

      {solutions.length > 0 && (
        <div className="solutions">
          <h2>Solutions:</h2>
          {solutions.map((solution, index) => (
            <div key={index} className="solution">
              <p>Solution {index + 1}:</p>

<div className="matrix" >
  
  {solution && solution.map((row, rowIndex) => (
    <div key={rowIndex} className="matrix-row">
      {row && row.map((cell, colIndex) => (
        <span key={colIndex} className="matrix-cell">
          {cell === 1 ? '  ♛  ' : '    '}
        </span>
      ))}
    </div>
  ))}
</div>



            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;