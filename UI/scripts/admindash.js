
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
            addRow('admintable',parcelname,parcelid);
        }
    })
}


function addRow(tableID,parcelName,parcelid) {
    let tableRef = document.getElementById(tableID);
    let newRow = tableRef.insertRow(-1);

    let parcelname = newRow.insertCell(0);
    let parcelID = newRow.insertCell(1);
    let details = newRow.insertCell(2);
    
    let newParcel = document.createTextNode(parcelName);
    let newid = document.createTextNode(parcelid);
    var button2 = document.createElement("button");
    button2.innerHTML = "Edit status";
    button2.addEventListener('click',()=>{
        var forminput = '<input type="text" id="editstatus" required="required">'
        document.getElementById('presentlocation').innerHTML = forminput
    })
    var button3 = document.createElement("button");
    button3.innerHTML = "Edit location";
    button3.addEventListener('click',()=>{
        var forminput2 = '<input type="text" id="editlocation" required="required">'
        document.getElementById('presentlocation').innerHTML = forminput2
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

    parcelname.appendChild(newParcel);
    parcelID.appendChild(newid);
    details.appendChild(button);
  }

function updateOrder(){
    let newstatus = document.getElementById('editstatus').value;
    let newlocation = document.getElementById('editlocation').value;
    if(!!newlocation){
        alert('what the hell');
        }
    alert(newlocation);
}  