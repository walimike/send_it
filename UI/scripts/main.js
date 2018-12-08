token = localStorage.getItem("accesstoken")
function updateProfile(url,tableID){
    fetch(url, {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
        }
    })
    .then(res => res.json())
    .then(response => {
        data = response.Parcels
        statusArray =[]
        var i;
        for (i = 0; i < data.length; i++) { 
            specificParcel = data[i];
            let newRow = document.getElementById(tableID).insertRow(-1);
            newRow.insertCell(0).appendChild(document.createTextNode(specificParcel.parcel_name));
            newRow.insertCell(1).appendChild(document.createTextNode(specificParcel.parcelid));
            newRow.insertCell(2).appendChild(document.createTextNode(specificParcel.parcel_destination));
            newRow.insertCell(3).appendChild(document.createTextNode(specificParcel.parcel_source));
            newRow.insertCell(4).appendChild(document.createTextNode(specificParcel.parcel_status));
            newRow.insertCell(5).appendChild(document.createTextNode(specificParcel.present_location));
            newRow.insertCell(6).appendChild(document.createTextNode(specificParcel.price));
            if (tableID=='profiletable'){
                newRow.insertCell(7).appendChild(document.createTextNode(specificParcel.usrid));
                newRow.insertCell(8).appendChild(document.createTextNode(specificParcel.username));
            }
            else{
                document.getElementById('userprofilename').innerText= specificParcel.username;
                document.getElementById('userprofileid').innerText= specificParcel.usrid;    
            } 
            statusArray.push(specificParcel.parcel_status)          
       }
        intransit = statusArray.filter(function(value){
            return value === 'In Transit';
        }).length
        delivered = statusArray.filter(function(value){
            return value === 'delivered';
        }).length
        document.getElementById('totaldelivered').innerText= delivered;
        document.getElementById('totalintransit').innerText= intransit;
    })
}

function Logout() {
    localStorage.removeItem('token');
    window.location.href = 'index.html';
}

function logIn() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    
    const url = 'https://challenge4.herokuapp.com/v2/api/auth/login';

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

function signUp() {
    let username = document.getElementById('username').value;
    let password1 = document.getElementById('password1').value;
    let password2 = document.getElementById('password2').value;
    let email = document.getElementById('email').value;
    
    if (password1 != password2){
        alert('Passwords do not match')
    }

    const url = 'https://challenge4.herokuapp.com/v2/api/auth/signup';

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
        if (response.message=="you have successfully signed up as " + username){
        window.location.replace('index.html');
        }
    })
}
    
<div class="modal">
    <div class="modal-content">
        <span class="close-button">&times;</span>
        <h1 id="message">Hello, I am a modal!</h1>
    </div>        
</div>

function userAlert(message){

var modal = document.querySelector(".modal");
    var trigger = document.querySelector(".trigger");
    var closeButton = document.querySelector(".close-button");

    function toggleModal() {
        modal.classList.toggle("show-modal");
    }

    function windowOnClick(event) {
        if (event.target === modal) {
            toggleModal();
        }
    }

    trigger.addEventListener("click", toggleModal);
    closeButton.addEventListener("click", toggleModal);
    window.addEventListener("click", windowOnClick);        
}