const togglePassword = document.getElementById('togglePassword');
const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirmPassword');
const form = document.getElementById('signupForm');
const errorMessage = document.getElementById('error-message');

// Toggle password visibility
togglePassword.addEventListener('click', function () {
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    this.textContent = type === 'password' ? '👁️' : '🙈';
});

// Form validation on submit
form.addEventListener('submit', function (event) {
    event.preventDefault();
    errorMessage.style.display = 'none';  // Reset error message display

    // Check if all fields are filled
    if (!password.value || !confirmPassword.value || !document.getElementById('name').value || 
        !document.getElementById('mobile').value || !document.getElementById('email').value) {
        errorMessage.textContent = 'Please fill in all fields.';
        errorMessage.style.display = 'block';
        return;
    }

    // Check if passwords match
    if (password.value !== confirmPassword.value) {
        errorMessage.textContent = 'Passwords do not match.';
        errorMessage.style.display = 'block';
        return;
    }

    // Create and populate FormData inside the submit event
    const formData = new FormData();
    formData.append('name', document.getElementById('name').value);
    formData.append('mobile_number', document.getElementById('mobile').value);
    formData.append('email', document.getElementById('email').value);
    formData.append('password', password.value);

    // Send form data to the backend
    fetch('/store_user_information', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Successful signup');
            errorMessage.textContent = data.message;
            
            window.location.href = '/login_page';
        } else {
            errorMessage.textContent = data.message || 'Signup failed';
            errorMessage.style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        errorMessage.textContent = 'An error occurred. Please try again.';
        errorMessage.style.display = 'block';
    });
});
