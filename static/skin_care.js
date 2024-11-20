let for_image = document.getElementById("image_file");
let for_prompt = document.getElementById("input_quary");
let for_skin_type = document.getElementById("type_of_skin");
let answer = document.getElementById("answer");
console.log("hi");

let button = document.getElementById("button");

button.addEventListener('click', () => {
    const formData = new FormData();
    formData.append('image', for_image.files[0]);
    formData.append('prompt', for_prompt.value);
    formData.append('skin', for_skin_type.value);

    fetch('/skin_care', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        let advise = data.ai_response;  // Expecting JSON response with a 'tips' field
        answer.innerText = advise;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
