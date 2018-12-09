token = localStorage.getItem("accesstoken")
const orderUrl = 'http://127.0.0.1:5000/v2/api/parcels';
const userOrderUrl = 'http://127.0.0.1:5000/v2/api/users/parcels';

function getAllOrders() {
    
    fetch(orderUrl, {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
        }
    })
    .then(res => res.json())
    .then(response => {
        data = response.Parcels
        var i;
        for (i = 0; i < data.length; i++) { 
            specificParcel = data[i];
            parcelname = specificParcel.parcel_name;
            parcelid = specificParcel.parcelid;
            username = specificParcel.username
            addRow('admintable',parcelname,username,parcelid);
        }
    })
}

function addRow(tableID,parcelName,username,parcelid) {
    let newRow = document.getElementById(tableID).insertRow(-1);

    let newParcel = document.createTextNode(parcelName);
    let newid = document.createTextNode(username);
    var button2 = document.createElement("button");
    button2.innerHTML = "Edit status";
    button2.addEventListener('click',()=>{
        document.getElementById('status').innerHTML = `<input type="text" onblur=updateStatus(event,${parcelid}) id="editstatus" required>`
        button2.innerHTML = "Save";
        
    })
    var button3 = document.createElement("button");
    button3.innerHTML = "Edit location";
    button3.addEventListener('click',()=>{ 
        document.getElementById('presentlocation').innerHTML = `<input type="text" onblur=updateLocation(event,${parcelid}) id="editlocation" required>`
        button3.innerHTML = "Save";
    })
    var button = document.createElement("button");
    button.innerHTML = "Details";
    button.addEventListener('click',()=>{
        const specificOrder = `http://127.0.0.1:5000/v2/api/parcels/${parcelid}`;
        fetch(specificOrder, {
            method: 'GET',
            mode: 'cors',
            headers: {
                     'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
                 }
             })
        .then(res => res.json())
        .then(response => {
            data = response.Parcel[0];
            document.getElementById('parcelname').innerText= data.parcel_name;
            document.getElementById('price').innerText= data.price;
            document.getElementById('source').innerText= data.parcel_source;
            document.getElementById('presentlocation').innerText= data.present_location;
            document.getElementById('destination').innerText= data.parcel_destination;
            document.getElementById('status').innerText= data.parcel_status;
            document.getElementById('statusbutton').appendChild(button2);
            document.getElementById('locationbutton').appendChild(button3);
         })
    });

    newRow.insertCell(0).appendChild(newParcel);
    newRow.insertCell(1).appendChild(newid);
    newRow.insertCell(2).appendChild(button);
  }

  function updateLocation(e,parcelid){
    locationurl = `http://127.0.0.1:5000/v2/api/parcels/${parcelid}/presentlocation`
    newlocation=e.target.value;

    let data = {
        present_location:newlocation
    }
    fetch(locationurl, {
        method: 'PUT',
        mode: 'cors',
        headers: {
                 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
             },
        body: JSON.stringify(data)     
         })
    .then(res => res.json())
    .then(response => {
        alert(response.message)
        document.location.reload(true);
    })
  }

  function updateStatus(e,parcelid){  
    statusurl = `http://127.0.0.1:5000/v2/api/parcels/${parcelid}/cancel`
    newstatus=e.target.value;
    if( (newstatus=='cancel') || (newstatus=='deliver') ) { 
        let data = {
            status:newstatus
        }
        fetch(statusurl, {
            method: 'PUT',
            mode: 'cors',
            headers: {
                    'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
                },
            body: JSON.stringify(data)     
            })
        .then(res => res.json())
        .then(response => {
            alert(response.message)
            document.location.reload(true);
        })
    }
    else{
        alert("status can only be cancel or deliver");
        return;
    }
}

