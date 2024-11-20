let hair_type=document.getElementById("type_hair")
let weather=document.getElementById("weather")
let button=document.getElementById("button")
let answer=document.getElementById("answer")

button.addEventListener('click',()=>{
    console.log('hi');
    
    const data={
        hair_type:hair_type.value,
        weather:weather.value
    }
    fetch('/hair_care',{
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body:JSON.stringify(data)
    }

    )
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