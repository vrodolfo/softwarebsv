var interval;
// $(document).on('mousemove keyup keypress',function(){
//     clearTimeout(interval);//clear it as soon as any event occurs
//   //do any process and then call the function again
//     settimeout();//call it again
// })
settimeout();
function settimeout(){
    interval=setTimeout(
        function(){
                    //console.log("Check is session is expired"); 
                    checkSession();
                  },600000)
}


window.setInterval(function(){
    var r = confirm("Tu sesion esta por expirar, deseas extenderla?");
    if (r == true) {
        clearTimeout(interval);
        checkSession();
        settimeout();

    } else {
        //Leve the timer to finish
    }

}, 420000);


function checkSession() {
    var request = false;
    if(window.XMLHttpRequest) { // Mozilla/Safari
        request = new XMLHttpRequest();
    } else if(window.ActiveXObject) { // IE
        request = new ActiveXObject("Microsoft.XMLHTTP");
    }
    request.open('GET', '/sessions/check/', true);
    request.onreadystatechange = function() {
        if(request.readyState == 4) {
            //console.log(request.responseText);
            if (request.responseText == "Valid") {
                // DO SOMETHING IF SESSION IS VALID
            
            } else {
                window.location = "/sessions/new";
            }
        }
    }
    request.send(null);
}

