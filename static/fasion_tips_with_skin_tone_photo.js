const input_image = document.getElementById('imageid');
const button = document.getElementById('button');
const spinner = document.getElementById('loadingSpinner');  // Get the spinner element
const messageDiv = document.getElementById('message');

button.addEventListener('click', () => {

    const file = input_image.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        // Show the spinner when the request starts
        spinner.style.display = 'block';
        messageDiv.innerText = '';  // Clear previous messages

        // Sending image to the backend via Fetch API
        fetch('/fasion_tips_with_skin_tone_photo', {
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
            spinner.style.display = 'none';
            // Display the result
            messageDiv.innerText = data.ai_response;
        })
        .catch(error => {
            // Hide the spinner if an error occurs
            spinner.style.display = 'none';
            messageDiv.innerText = "Error occurred: " + error.message;
            console.error("Error:", error);
        });
    } else {
        messageDiv.innerText = "Please select an image.";
    }
});
