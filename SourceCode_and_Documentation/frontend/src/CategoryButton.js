import React from "react";
import "./CategoryButton.css";

import Artsy from "./icons/artsy.png";
import Delicious from "./icons/delicious.png";
import Family from "./icons/family.png";
import Geeky from "./icons/geeky.png";
import History from "./icons/history.png";
import Indoor from "./icons/indoor.png";
import Ouside from "./icons/outside.png";
import Romantic from "./icons/romantic.png";
import Sporty from "./icons/sporty.png";

const icons = {
  "family-friendly": Family,
  artsy: Artsy,
  delicious: Delicious,
  geeky: Geeky,
  historic: History,
  indoors: Indoor,
  outdoors: Ouside,
  romantic: Romantic,
  sporty: Sporty
};

export const CategoryButton = props => {
  const { category, onClick } = props;

  return (
    <div className="category-button" onClick={onClick}>
      <div className="category-text text">
        {category} <img className="category-image" src={icons[category]}></img>
      </div>
    </div>
  );
};
