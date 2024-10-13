import { useEffect, useState } from 'react';

const History = () => {
  const [data, setData] = useState(null);

  const obtener = async () => {
    try {
      const res = await fetch('http://127.0.0.1:5000/api/data');
      if (!res.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await res.json();
      setData(data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    obtener();
  }, []);

  return (
    <div class="flex flex-col items-center justify-center h-screen">
      <h1>History</h1>
      {data ? (<h2>{data.message}</h2>) : (<p>Loading...</p>)}
    </div>
  );
};

export default History;
