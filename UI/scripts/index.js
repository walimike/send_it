function logIn() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    
    const url = 'https://walimike-sendit2.herokuapp.com/v2/api/auth/login';

    let data = {
        name: username,
        password: password
    }
    fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        localStorage.setItem("accesstoken",response.access_token);
        alert(response.message);
        if (response.role=='user'){
            window.location.replace('userhome.html');
        }
        else{
            window.location.replace('adminhome.html');
        }
    })
}