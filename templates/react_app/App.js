import React, { useState, useEffect } from "react";
import { fetchSomeData } from "./api";

const centerContentStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

export const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchSomeData().then((data) => setData(data));
  }, []);

  if (data.length < 1)
    return <h1 style={centerContentStyle}>No data provided...</h1>;

  return (
    <div style={centerContentStyle}>
      {Object.entries(data).map((entry) => (
        <div>
          {entry[0]}: {entry[1]}
        </div>
      ))}
    </div>
  );
};

export default App;
