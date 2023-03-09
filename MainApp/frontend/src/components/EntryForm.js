import React  from 'react'



const EntryForm = (props) => {
    let [date, amount, description] = React.useState(0,0,0);
 
    const accountURL = "http://localhost:8000/Accounts_POST/l;kj"
    const altURL = "http://127.0.0.1:8000/Accounts_POST/dfgsdfg"
 
    const updateDate = (event) => {
       date = event.target.value
       console.log(event.target.value)
    }
    
    const updateAmount = (event) =>{
 
       amount = event.target.value
       console.log(amount)
    }
    
    const updateDescription = (event) => {
       description = event.target.value
       console.log(event.target.value)
    }
 
    const handleSubmit = (event) => {
       console.log("Submit Triggers")
       event.preventDefault(); 
 
    // let entryLine = {
    //       "date" : date,
    //       "amount" : amount, 
    //       "description" : description
    //    }
       
 
      fetch(accountURL,{
          'Method' : 'POST', 
          'Headers' : {
            'Content-Type' : 'applicaiton/json'
          },
          'Body' : JSON.stringify({date, amount, description})
       }).then(response => response.json())
       .then(data => {
         console.log('Success:', data);
       })
       .catch((error) => {
         console.error('Error:', error);
       });
       
    }
 
    return (
        <div>
        <h1> Entry Point</h1>
        <form onSubmit={handleSubmit}>
           <label>Date</label>
           <input type="date" id="date" onChange={updateDate}></input>
           <label>Amount</label>
           <input type="number" id="amount" onChange={updateAmount}></input>
           <label>Description</label>
           <input type="text" id="description" onChange={updateDescription}></input>
            <input type="submit" value="Submit" />
          </form>
        </div>
    )
 
 }

 export default EntryForm; 