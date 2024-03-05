import React, { useState } from 'react'

export default function Signup({user, handleUser}) {

    const [ username, setUsername ] = useState("")
    const [ password, setPassword ] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault()

        const submitVal = {
            "name": username,
            "password": password
        }

        console.log("submitting val", submitVal)

        fetch("/signup",{
            method:"POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(submitVal)
        })
        .then(resp=> resp.json())
        .then(signedUpUserFromServer => {
                console.log("signedUpUserFromServer---", signedUpUserFromServer)
                handleUser(signedUpUserFromServer)
                setUsername("")
                setPassword("")
            })
        .catch(console.error)
    }


    return (
            <>
                <form onSubmit= {handleSubmit}>
                    <label>
                        name
                    </label>

                    <input
                        type='text'
                        name='username'
                        value={username}
                        onChange={(e)=>setUsername(e.target.value)}/>

                    <label>
                        password
                    </label>
                    
                    <input
                        type='text'
                        name='password'
                        value={password}
                        onChange={(e)=>setPassword(e.target.value)}/>

                    <button type = 'submit'> Signup </button>
                </form>
            </>
        )
}
