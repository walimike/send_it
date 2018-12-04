/*{
    "parcel_destination": "jdfdk",
    "parcel_name": "hadsagds",
    "parcel_source": "jkgfhdfh",
    "parcel_status": "In Transit",
    "parcelid": 1,
    "present_location": "Unknown",
    "price": 123456,
    "usrid": 3
},*/

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
            data = response.Parcel;
            document.getElementById('parcelname').innerText= data.parcel_name;
            document.getElementById('price').innerText= data.price;
            document.getElementById('status').innerText= data.parcel_name;
            
         })
    });

    parcelname.appendChild(newParcel);
    parcelID.appendChild(newid);
    details.appendChild(button);
  }
