var x = false;

function Toggle(){
	x = !x;
	document.querySelector(".sidenav").hidden = !document.querySelector(".sidenav").hidden;
	if(x==true){
		document.getElementById("content").classList.remove("content");
		document.getElementById("content").classList.add("shrink");
	}
	else
	{
		document.getElementById("content").classList.remove("shrink");
		document.getElementById("content").classList.add("content");
	}
}