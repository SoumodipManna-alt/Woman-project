console.log("hi");

let input=document.getElementById("input")
let button=document.getElementById("button")
let answer=document.getElementById("answer")



function convertToSimpleText(input) {
    let formattedText = input
    .replace(/\*\*(.*?)\*\*/g, '$1')  // Remove **bold** formatting
    .replace(/\*(.*?)\*/g, '$1')      // Remove *italic* formatting
    .replace(/•/g, "-")               // Replace bullet points with dashes for readability
    .replace(/\n/g, " ")              // Remove newlines and replace them with spaces
    .replace(/\s+/g, ' ')             // Remove excess spaces
    .trim();                         // Trim leading/trailing spaces

    return formattedText;
}


button.addEventListener('click',()=>{

    const Month = {
        month: input.value
    };
    console.log(Month.month);
    
    fetch('/pregnency_tracker', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(Month)
    })
    .then(response => response.json())
    .then(data => {
        // Get advice and format it
        let advise = data.tips;  // Already in text format, no need for JSON.stringify
        //let ans=convertToSimpleText(advise)
        //console.log(advise);
        
        //console.log(ans);

        answer.innerText=advise
})
})