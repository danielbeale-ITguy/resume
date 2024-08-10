
function updatedcount(){
    const xhttp = new XMLHttpRequest();
    xhttp.open("GET", "https://danssecondtest.azurewebsites.net/api/testingfun?code=ailjqqnYThtm44lVTd5kxxYJU4p-qITeemkDSQB7GzdUAzFuGYSG4Q%3D%3D", true)
    xhttp.onreadystatechange = function(){
        const responseText = this.responseText;
        const count = responseText.split('Count: ')[1];
        document.getElementById("countlabel").innerHTML = count;
    };
        xhttp.send();
}


