import React, { useState, useEffect } from 'react';

import { GetProducts } from "./helper/coreapicalls";
import Base from "./Base";

import "../styles.css";
import Card from "./Card";

export default function Home() {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(false);

  const loadAllProducts = () => {
    GetProducts()
      .then((data) => {
        if (data.error) {
          setError(data.error)
          console.log(error)
        } else{
          setProducts(data);
        }
      })
      .catch(err => console.log(err))
  }

  useEffect(() => {
    loadAllProducts();
  });

  return(
    <Base className="text-center" title="Home Page" description="Welcome to my T-shirt Store">
      <h1>Home Component</h1>
      <div className="row">
        {products.map((product, index) => {
          return (
            <div key={index} className="col-4 mb-4">
              <Card product={product}/>
            </div>
          );
        })}
      </div>
    </Base>
  );
}
