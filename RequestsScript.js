


//Request for different end points

/*
**REQUEST
 */

fetch("http://localhost:8000/profiles", {
    method: "GET",
    header: {
        "Content-Type": "application/json"
    }
})
    .then(response => reponse.json())
    .then(data => console.log(data))
    .catch(error => console.error(error))