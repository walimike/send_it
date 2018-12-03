function signUp() {
    let username = document.getElementById('username').value;
    let password1 = document.getElementById('password1').value;
    let password2 = document.getElementById('password2').value;
    let email = document.getElementById('email').value;
    
    if (password1 != password2){
        alert('Passwords do not match')
    }

    const url = 'http://127.0.0.1:5000/v2/api/auth/signup';

    let data = {
        name: username,
        email: email,
        password: password1
    }
    fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        alert(response.message);
        if (response.message=="you have successfully signed up as" + username){
        window.location.replace('index.html');
        }
    })
}
    