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
    let parcelid = newRow.insertCell(4);
  
    let newParcel = document.createTextNode(parcelName);
    let parcelSource = document.createTextNode(source);
    let parcelDestination = document.createTextNode(destination);
    let parcelPrice = document.createTextNode(price);
    let parcel_id = document.createTextNode(parcelID);

    parcelname.appendChild(newParcel);
    parcelsource.appendChild(parcelSource);
    parceldestination.appendChild(parcelDestination);
    parcelprice.appendChild(parcelPrice);
    parcelid.appendChild(parcel_id);
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
        data = response.Parcel
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

function showDetails(){
    let parcelid = document.getElementById('parcelid').value;
    const specificOrderUrl = `http://127.0.0.1:5000/v2/api/parcels/${parcelid}`
    fetch(specificOrderUrl, {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
        }
    })
    .then(res => res.json())
    .then(response => {
        data = response.Parcel
        specificParcel = data[0];
        parcelname = specificParcel.parcel_name;
        source = specificParcel.parcel_source;
        destination = specificParcel.parcel_destination;
        price = specificParcel.price
        parcel_id = specificParcel.parcelid
        addDetails(parcelname,source,destination,price,parcel_id)
        //alert(data)
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