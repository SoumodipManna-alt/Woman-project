let image=document.getElementById("image")
let oca_event=document.getElementById("event")
let button=document.getElementById("button")
let message=document.getElementById("message")

button.addEventListener('click', ()=>{
let file=image.files[0]
const formdata=new FormData()
formdata.append('image',file)
formdata.append('event',oca_event.value)
url='/occasion_wise_outfit'
fetch(url,
    {
        method:'POST',
        body:formdata
    }
)
.then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
})
.then(data=>{
    message.innerText=data.ai_response 
})
.catch(error => {
    console.error('Error:', error);
});

})
