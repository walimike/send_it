document.getElementById('signupForm').addEventListener('submit', registerUser);
const url = 'https://walimike-sendit2.herokuapp.com/v2/api/auth/signup';

function registerUser(event){
    event.preventDefault();

    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let password1 = document.getElementById('password1').value;
    let password2 = document.getElementById('password2').value;
    let role = document.getElementsById('user-type').value;

    if (password1 != password2){
        alert("passwords do not match")
    }
    let data = {
        username: username,
        email: email,
        password: password1,
        role: role
    }

    fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        console.log(response);
        if (response.message === 'you have successfully signed up') {
            alert(`You have registered as ${data['username']}`);
            window.location.replace('index.html');
        } else {
            alert(response.message);
        }
    })
    .catch(err => console.log(err));
}
d
function signUp() {
    alert("Successfully signed up, go to log in"+role);
}
