console.log("hi");
let arr = [];

// Check if "phone_no" exists in localStorage
if (localStorage.getItem("phone_no") !== null) {
    arr = JSON.parse(localStorage.getItem("phone_no"));
} else {
    localStorage.setItem("phone_no", JSON.stringify([]));
}
for(let i of arr){
    create_all_element(i, contactList);
}

function create_all_element(phoneNumber, contactList) {
    const contactItem = document.createElement('div');
    contactItem.classList.add('contact-item');

    // Create radio button
    const radio = document.createElement('input');
    radio.type = 'radio';
    radio.name = 'contact';
    radio.value = phoneNumber;  // Set phone number as the value

    // Create text input for phone number (read-only)
    const contactNumber = document.createElement('input');
    contactNumber.type = 'email';
    contactNumber.value = phoneNumber;

    // Create remove button
    const removeBtn = document.createElement('button');
    removeBtn.classList.add('remove-btn');
    removeBtn.textContent = 'Remove';

    // Append elements to contact item
    contactItem.appendChild(radio);
    contactItem.appendChild(contactNumber);
    contactItem.appendChild(removeBtn);

    // Append contact item to contact list
    contactList.appendChild(contactItem);

    phoneInput.value = '';  // Clear input field

    // Add event listener to remove button
    removeBtn.addEventListener('click', function() {
        contactList.removeChild(contactItem);
    });
}

// Event listener for the Add Contact button
document.getElementById('addContactBtn').addEventListener('click', function() {
    const phoneInput = document.getElementById('phoneInput');
    const contactList = document.getElementById('contactList');
    const phoneNumber = phoneInput.value.trim();

    if (phoneNumber === '') {
        alert("Please enter a Email.");
        return;
    }

    arr = JSON.parse(localStorage.getItem("phone_no"));
    if (Array.isArray(arr)) {
        arr.push(phoneNumber);
        localStorage.setItem("phone_no", JSON.stringify(arr));
    } else {
        arr = [phoneNumber];
        localStorage.setItem("phone_no", JSON.stringify(arr));
    }

    create_all_element(phoneNumber, contactList);
    console.log(arr);
});

document.querySelector(".contact-list").addEventListener('click',(e)=>{
    let parent_element=e.target.parentElement
    // console.log(current_element);
    let current_element=e.target.previousElementSibling.value
    if(arr.includes(current_element)){
        arr=arr.filter((c)=>{
            return c!=current_element
        })
    }
    localStorage.setItem("phone_no",JSON.stringify(arr))
    console.log(arr);

    /// fatch location     


    
    
})


// Function to get selected contact
function getSelectedContact() {
    const contacts = document.getElementsByName('contact');
    let selectedValue = null;

    for (const contact of contacts) {
        if (contact.checked) {
            selectedValue = contact.value;
            break;
        }
    }

    return selectedValue;
}

// Function to get location and send data to backend
function sendLocationToBackend() {
    const locationElement = document.getElementById("location");
    const selectedContact = getSelectedContact();

    if (!selectedContact) {
        alert("Please select a email.");
        return;
    }

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;

                // Prepare data to send to the backend
                const data = {
                    contact: selectedContact,
                    location: {
                        latitude: latitude,
                        longitude: longitude
                    }
                };

                // Send data to the backend
                fetch('/your_safty', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(result => {
                    alert( result.message);
                    locationElement.innerText = `Location sent: Latitude: ${latitude}, Longitude: ${longitude}`;
                })
                .catch(error => {
                    alert(result.message);
                });
            },
            (error) => {
                switch (error.code) {
                    case error.PERMISSION_DENIED:
                        locationElement.innerText = "User denied the request for Geolocation.";
                        break;
                    case error.POSITION_UNAVAILABLE:
                        locationElement.innerText = "Location information is unavailable.";
                        break;
                    case error.TIMEOUT:
                        locationElement.innerText = "The request to get user location timed out.";
                        break;
                    default:
                        locationElement.innerText = "An unknown error occurred.";
                        break;
                }
            }
        );
    } else {
        locationElement.innerText = "Geolocation is not supported by this browser.";
    }
}

document.getElementById("need_help").addEventListener('click',()=>{
    sendLocationToBackend()
})