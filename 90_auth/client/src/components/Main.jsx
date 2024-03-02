import React, { useState, useEffect } from 'react'
import Signup from './Signup'
import Logout from './Logout'
import Login from './Login'

export default function Main() {

    const [ user, setUser ] = useState({})

    useEffect(()=> {
        //auto-login
        fetchUser()
    }, [])

    const handleUser = (signedUpOrLogOutUser) => {
        setUser(signedUpOrLogOutUser)
        fetchUser()
    }

    const fetchUser = () => {
        fetch("/check_session")
            .then(res => {
                if(res.ok){
                    res.json()
                    .then(userfromsession => {
                        console.log("user from session -- ", userfromsession)
                        setUser(userfromsession)
                    })
                }else{
                    setUser({})
                }
            })
    }

    useEffect(() => {
        console.log("current user: ", user)
    }, [user]) //to see the current user


    return (
        <>
            <Signup 
                user = {user}
                handleUser={handleUser}
                />

            <Logout 
                handleUser={handleUser}
                />

            <Login
                user = {user}
                handleUser={handleUser}
                />                
        </>
        
    )
}
