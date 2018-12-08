token = localStorage.getItem("accesstoken")
const orderUrl = 'http://127.0.0.1:5000/v2/api/parcels';
const userOrderUrl = 'http://127.0.0.1:5000/v2/api/users/parcels';

function makeOrder() {
    
    let parcelname = document.getElementById('parcelname').value;
    let price = document.getElementById('price').value;
    let source = document.getElementById('source').value;
    let destination = document.getElementById('destination').value;

    let data = {
        parcel_name: parcelname,
        source: source,
        destination: destination,
        price: parseInt(price, 10) 
    }

    fetch(orderUrl, {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        alert(response.message);
      if (response.message=='order added successfully'){
        addRow('parceltable',parcelname,source,destination,price,100)
      }  
    })
}

function addRow(tableID,parcelName,source,destination,price,parcelID) {
    let tableRef = document.getElementById(tableID);
    let newRow = tableRef.insertRow(-1);

    let parcelname = newRow.insertCell(0);
    let parcelsource = newRow.insertCell(1);
    let parceldestination = newRow.insertCell(2);
    let parcelprice = newRow.insertCell(3);
    let button = newRow.insertCell(4);
  
    let newParcel = document.createTextNode(parcelName);
    let parcelSource = document.createTextNode(source);
    let parcelDestination = document.createTextNode(destination);
    let parcelPrice = document.createTextNode(price);
    var newbutton = document.createElement("button");
    newbutton.innerHTML = "Details";

    newbutton.addEventListener('click',()=>{
        fetch(`http://127.0.0.1:5000/v2/api/parcels/${parcelID}`, {
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
            }
        })
        .then(res => res.json())
        .then(response => {
            data = response.Parcel[0] 
            document.getElementById('userparcelname').innerText= data.parcel_name;
            document.getElementById('userprice').innerText= data.price;
            document.getElementById('usersource').innerText= data.parcel_source;
            document.getElementById('userlocation').innerText= data.present_location;
            document.getElementById('userdestination').innerText= data.parcel_destination;   
            var button4 = document.createElement("button");
            button4.innerHTML = "Edit";
            button4.addEventListener('click',()=>{ 
                document.getElementById('userdestination').innerHTML = `<input type="text" onblur=updateDestination(event,${data.parcelid}) id="userdestination" required>`
                button4.innerHTML = "Save";
            })
            document.getElementById('userbutton').appendChild(button4);
         })
        
    });
    parcelname.appendChild(newParcel);
    parcelsource.appendChild(parcelSource);
    parceldestination.appendChild(parcelDestination);
    parcelprice.appendChild(parcelPrice);
    button.appendChild(newbutton)
  }

function fetchAll(){
    fetch(userOrderUrl, {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
        }
    })
    .then(res => res.json())
    .then(response => {
        data = response.Parcels;
        var i;
        for (i = 0; i < data.length; i++) { 
            specificParcel = data[i];
            parcelname = specificParcel.parcel_name;
            source = specificParcel.parcel_source;
            destination = specificParcel.parcel_destination;
            price = specificParcel.price
            parcel_id = specificParcel.parcelid
            addRow('parceltable',parcelname,source,destination,price,parcel_id)
        }
    })  
    
}  

function addDetails(parcelname,source,destination,price,parcel_id){
    let tableRef = document.getElementById('detailstable');
    let newRow = tableRef.insertRow(-1);

    let parcelname = newRow.insertCell(0);
    let parcelsource = newRow.insertCell(1);
  
    let newParcel = document.createTextNode('Parcel Name');
    let parcelSource = document.createTextNode(parcelName);
    
    parcelname.appendChild(newParcel);
    parcelsource.appendChild(parcelSource);
}

function updateDestination(e,parcelid){
    statusurl = `http://127.0.0.1:5000/v2/api/parcels/${parcelid}/destination`
    newdestination=e.target.value;
    let data = {
        destination:newdestination
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

