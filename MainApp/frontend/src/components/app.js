import React, { Component } from "react";
import { render } from "react-dom"
import Homepage from "./Homepage"



function App (){
    return (
        <div>
            <Homepage />
        </div>
    );
  }

const root = document.getElementById("root")
render(<App />, root)

export default App;

