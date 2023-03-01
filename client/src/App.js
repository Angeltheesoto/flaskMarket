import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    let fetchData = async () => {
      await fetch("/members")
        .then((res) => res.json())
        .then((data) => {
          setData(data);
          console.log("Data fetched succussfully: ", data);
        })
        .catch((err) => console.log("Error: ", err));
    };
    fetchData();
  }, []);

  return (
    <div className="App">
      {typeof data.members === "undefined" ? (
        <p>loading..</p>
      ) : (
        data.members.map((member, i) => {
          return <p key={i}>{member}</p>;
        })
      )}
    </div>
  );
}

export default App;
