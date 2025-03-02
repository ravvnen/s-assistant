// src/App.tsx
import React, { useEffect, useState } from 'react';

interface Building {
  id: number;
  name: string;
  bestRanking: string;
}

const App: React.FC = () => {
  const [buildings, setBuildings] = useState<Building[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Replace with your Flask API endpoint for buildings
    fetch('http://localhost:5000/api/buildings')
      .then((res) => res.json())
      .then((data) => {
        // Assuming data is an array of { id, name, bestRanking }
        setBuildings(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Error fetching buildings:', err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Building Rankings</h1>
      <table style={{ borderCollapse: 'collapse', width: '100%' }}>
        <thead>
          <tr>
            <th style={{ border: '1px solid #333', padding: '8px' }}>ID</th>
            <th style={{ border: '1px solid #333', padding: '8px' }}>Name</th>
            <th style={{ border: '1px solid #333', padding: '8px' }}>Best Ranking</th>
          </tr>
        </thead>
        <tbody>
          {buildings.map((building) => (
            <tr key={building.id}>
              <td style={{ border: '1px solid #333', padding: '8px' }}>
                <a
                  href={`https://mit.s.dk/studiebolig/building/${building.id}/`}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {building.id}
                </a>
              </td>
              <td style={{ border: '1px solid #333', padding: '8px' }}>
                <a
                  href={`https://mit.s.dk/studiebolig/building/${building.id}/`}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {building.name}
                </a>
              </td>
              <td style={{ border: '1px solid #333', padding: '8px' }}>
                {building.bestRanking}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default App;
