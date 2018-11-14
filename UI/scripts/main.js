function signUp() {
		alert("Successfully signed up, go to log in");
}		

function SelectUser(){
	if (document.getElementById('admin').checked){
		window.location.href ="adminhome.html";}
  else if (document.getElementById('user').checked){
		window.location.href ="userhome.html";}
}
