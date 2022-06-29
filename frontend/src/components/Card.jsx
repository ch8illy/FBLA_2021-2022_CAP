import React from "react";
import "./css/card.css";

/**
 * 
 * @param {*} props 
 * @returns card component which has all the useful information needed. 
 * Using react props to get data after filtering
 */

function Card (props) {
      return(
          <div className="card">
            <img src = {props.img} />
            <div className="card-body">
              <h1>{props.name}</h1>
              <p>{props.loc}  |  {props.address}</p>
              <p id = 'open'>Open: {props.times}</p>
              <h2>Contact:</h2>
              <p>Phone: {props.number}</p>
              <a href = {props.website} target = 'blank'>Website 🔗</a>
              <h5>{props.rating}/5 STARS ({props.reviews} reviews)</h5>
            </div>
          </div>
      )    
}

export default Card;