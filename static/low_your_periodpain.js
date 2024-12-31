let input = document.getElementById("symtoms");
let button = document.querySelector(".button");
let response = document.getElementById("answer");
const spinner = document.getElementById('loadingSpinner');

function convertAdviceToText(input) {
    // Step 1: Clean up the input by replacing special characters and adjusting formatting
    let formattedText = input
        .replace(/\\n/g, ' ')  // Replace newline characters with spaces
        .replace(/\\n\\n/g, '\n\n') // Replace double newlines for paragraph breaks
        .replace(/Advice no (\d+):/g, (match, number) => `${number}.`)  // Replace "Advice no X:" with numbered points
        .trim(); // Remove any leading/trailing spaces
    
    return formattedText;
}

button.addEventListener('click', () => {
    const symptomsData = {
        symptoms: input.value
    };
    // console.log(symptomsData.symptoms);
    button.disabled=true
    spinner.style.display = 'block';
    // messageDiv.innerText = ''; 
    fetch('http://localhost:5000/low_your_period_pain', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(symptomsData)
    })
    .then(response => response.json())
    .then(data => {
        // Get advice and format it
        let advise = data.Excercises;  // Already in text format, no need for JSON.stringify
        // console.log(advise);
       
        let advise1 = convertAdviceToText(advise);
        // console.log(advise1);
       
        response.innerText = advise;  // Display the formatted text
        spinner.style.display = 'none';
        button.disabled=false
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
