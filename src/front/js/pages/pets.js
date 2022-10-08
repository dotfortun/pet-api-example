import React, { useEffect, useState } from "react";
import { PetCard } from "../component/pet";

const PetsPage = () => {
  const [pets, setPets] = useState([]);

  useEffect(() => {
    setInterval(() => {
      fetch(process.env.BACKEND_URL + "/api/pets")
        .then((resp) => resp.json())
        .then((data) => setPets(data.pets));
    }, 1000);
  }, []);

  return (
    <div className="container">
      <div className="row">
        <div className="col col-10 offset-1 d-flex flex-row justify-content-between flex-wrap">
          {pets.map((elem, idx) => (
            <PetCard pet={elem} key={idx} />
          ))}
        </div>
      </div>
    </div>
  );
};

export { PetsPage };
