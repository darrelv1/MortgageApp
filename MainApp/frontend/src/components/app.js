import React, { Component, useState } from "react";
import { render } from "react-dom"
import Homepage from "./Homepage"
import {axios} from "axios"
import LayoutComponent from "./Layout"
import { BrowserRouter } from "react-router-dom";

let data;

const sampleAPIcall = (event) => {
    console.log("ACTIVE")
    
    const requestOptions = {
        method: 'GET'
    }
    fetch("http://localhost:8000/account/getLedgerByName/Claudia", requestOptions)
    .then(response => response.json())
    .then(response =>{ console.log(response)
     data =Object.keys(response[0])
     console.log(`This is console.log.${data}`)
    })

}





const App = () => {

   
    return (
        <BrowserRouter>
    <LayoutComponent>        
   
    </LayoutComponent>
    </BrowserRouter>
    );
  }

  

export default App;

