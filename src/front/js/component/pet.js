import React from "react";

const PetCard = ({ pet }) => {
  return (
    <div className="card" style={{ width: "30%" }}>
      <img
        src={`https://via.placeholder.com/300/${pet.profile_color}`}
        className="card-img-top"
      />
      <div className="card-body">
        <h5 className="card-title">{pet.name}</h5>
        <p className="card-text">
          {`${pet.name} is a ${pet.pet_color} ${pet.pet_type}. ` +
            `They are ${pet.age} years old, and are rated a solid ${pet.rating}/10.`}
        </p>
        <div className="card-footer text-muted">
          Last updated: {pet.updated}
        </div>
      </div>
    </div>
  );
};

export { PetCard };
