import React, { useState, useEffect } from 'react'
import CoffeeCard from './CoffeeCard'

export default function Coffee() {

    const [ coffees, setCoffees ] = useState([])

    useEffect(() => {
        fetch('/coffees')
            .then(resp => resp.json())
            .then(coffeeArr => {
                setCoffees(coffeeArr)})
            .catch(console.error)
    }, [])

    const coffeeCup = coffees.map((eachCoffee, idx) => {
       return <CoffeeCard cup = { eachCoffee } key={idx}/>
    })

  return (
   <>
       {coffeeCup}
   </>
  )
}