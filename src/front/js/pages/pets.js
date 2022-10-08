import React, { useEffect, useState } from "react";
import { PetCard } from "../component/pet";

const PetsPage = () => {
  const [pets, setPets] = useState([]);
  const [page, setPage] = useState(1);

  const decPage = () => {
    if (page > 1) {
      setPage(page - 1);
    }
  };

  useEffect(() => {
    setInterval(() => {
      fetch(process.env.BACKEND_URL + `/api/pets?page=${page}`)
        .then((resp) => resp.json())
        .then((data) => setPets(data.pets));
    }, 1000);
  }, []);

  return (
    <div className="container">
      <div className="row my-3">
        <div className="col col-10 offset-1 d-flex flex-row justify-content-around flex-wrap">
          <div className="btn-group" role="group" aria-label="navigation">
            <button
              onClick={() => setPage(page + 1)}
              type="button"
              className="btn btn-primary"
            >
              Next Page
            </button>
            <button onClick={decPage} type="button" className="btn btn-primary">
              Previous Page
            </button>
          </div>
        </div>
      </div>
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
