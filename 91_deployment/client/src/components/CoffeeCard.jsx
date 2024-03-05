import React from 'react'

export default function CoffeeCard( { cup }) {
    // console.log(cup)
  return (
    <>
        <h1>
            {cup.name}
        </h1>
        <h4>
            ${cup.price}
        </h4>
        <p>
            {cup.description}
        </p>

    </>
  )
}