let height=document.getElementById("height")
let weight=document.getElementById("weight")
let age=document.getElementById("age")
let button=document.getElementById("button")
const spinner = document.getElementById('loadingSpinner');

let answer=document.getElementById("answer")
console.log(height.value,weight.value,age.value);




button.addEventListener('click',()=>{
    const formdata=new FormData()
    formdata.append('height',height.value)
    formdata.append('weight',weight.value)
    formdata.append('age',age.value)
    button.disabled=true
    spinner.style.display = 'block';
    url='/diet_plan'
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
        spinner.style.display = 'none';
        button.disabled=false
    })
    .catch(error => {
        // Hide the spinner if an error occurs
        //spinner.style.display = 'none';
        messageDiv.innerText = "Error occurred: " + error.message;
        console.error("Error:", error);
    });
})