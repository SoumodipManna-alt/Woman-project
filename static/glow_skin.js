let image=document.getElementById("image_file")
let skin_type=document.getElementById("skin_type")
let button=document.getElementById("button")
let message=document.getElementById("answer")

button.addEventListener('click',()=>{
    const file=image.files[0]
    const formdata=new FormData()
    formdata.append('image',file)
    formdata.append('skin',skin_type.value)

    url='/glow_skin'
    fetch(url,{
        method:'POST',
        body : formdata
    })
    .then(response =>response.json())
    .then(data=>{
        message.innerText=data.ai_response

    })
    .catch(error => {
        console.error('Error:', error);
    });
})