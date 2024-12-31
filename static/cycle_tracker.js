// console.log("hi")
const spinner = document.getElementById('loadingSpinner');
document.getElementById('button').addEventListener('click',()=>{
const formData = new FormData();
formData.append('date',document.getElementById('inputdata').value)
button.disabled=true
    spinner.style.display = 'block';
const url='/cycle_traker'
fetch('/cycle_traker',{
     method: 'POST',
    body: formData
})
.then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
})
.then(data => {
    // Hide the spinner when the response is received
   // spinner.style.display = 'none';
    // Display the result
    answer.innerText = data.message;
    spinner.style.display = 'none';
    button.disabled=false
})
.catch(error => {
    // Hide the spinner if an error occurs
   // spinner.style.display = 'none';
    messageDiv.innerText = "Error occurred: " + error.message;
    console.error("Error:", error);
});
})