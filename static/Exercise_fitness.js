let height=document.getElementById("height")
let weigth=document.getElementById("weigth")
let age=document.getElementById("age")
let button=document.getElementById("button")

let answer=document.getElementById("answer")



button.addEventListener('click',()=>{
    const formdata=new FormData()
formdata.append('height',height.value)
formdata.append('weight',weigth.value)
formdata.append('age',age.value)

    url='/Exercise_fitness'
    fetch(url,{
        method:'POST',
        body:formdata
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data=>{
        answer.innerText=data.message
    })
    .catch(error => {
        // Hide the spinner if an error occurs
        spinner.style.display = 'none';
        messageDiv.innerText = "Error occurred: " + error.message;
        console.error("Error:", error);
    });
})