console.log("hi")
document.getElementById('button').addEventListener('click',()=>{
const formData = new FormData();
formData.append('date',document.getElementById('inputdata').value)
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
})
.catch(error => {
    // Hide the spinner if an error occurs
   // spinner.style.display = 'none';
    messageDiv.innerText = "Error occurred: " + error.message;
    console.error("Error:", error);
});
})