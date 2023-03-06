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


const LandingPage = (props) => {

    return (
        <div>
        <h1> Home: Landing PageDarel</h1>
        <button onClick={props.api}>API</button>
        
        DATA:
    
        </div>
    )
}

const Homepage = (props) =>{

    return (
       <Router>
            <Routes>
                <Route  path="create" element={<EntryForm/>}/>
                <Route  path="" element={<LandingPage api={props.apiCall} data={props.info}/>}/>
                <Route  path="profile" element={<ProfilePage />}/>   
            </Routes>
        </Router>
        )
    }

export default Homepage;




