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

    const coffeeCup = coffees.map((eachCoffee) => {
       return <CoffeeCard cup = { eachCoffee } />
    })

  return (
   <>
       {coffeeCup}
   </>
  )
}
