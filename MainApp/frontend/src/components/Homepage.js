import EntryForm from "./EntryForm"
import ProfilePage from "./profile"
import React from 'react'
import { 
    BrowserRouter as Router,
    Routes,
    Link,
    Route,
    Redirect,
} from 'react-router-dom'


const LandingPage = () => {

    return (
        <h1> Home: Landing Page</h1>
    )
}


const Homepage = (props) =>{

    return (
       <Router>
    <Routes>
    
        <Route  path="create" element={<EntryForm />}/>
        <Route  path="/" element={<LandingPage />}/>
        <Route  path="profile" element={<ProfilePage />}/>
        
    </Routes>
</Router>
        )
    }

export default Homepage;




