import React from 'react'

export default function Logout( {handleUser}) {

    const handleLogout = () => {
        fetch('/logout', {
            method: "DELETE"
        })
        .then(resp => {
            if (resp.ok){
                handleUser({})
            }})
    }

    return (
        <button onClick={handleLogout}> Logout </button>
    )
}
