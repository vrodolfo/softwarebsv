/*
//Se ejecuta solo al terminar de cargar la pagina

$(document).ready(function(){
	var x = $(".navbar"); 
	//lo oculto con visibility hidden y opacity 0 porque el display hidden no voy a poder meterle la transicion. Se ve feo sin la transicion
	$(x).css({"visibility":"hidden","opacity": "0"});

	$(window).scroll(function(){
		var actualPosition = $(window).scrollTop();
		if (actualPosition>=50){
			$(x).css({"visibility":"visible","opacity": "1", "transition":"all 400ms ease"});
		}	
		else{
			$(x).css({"visibility":"hidden","opacity": "0", "transition":"all 400ms ease" });
		}
	});
});

*/


$(document).ready(function(){

    //ScrollProcessor.process

	$('.owl-carousel').owlCarousel({
    loop:true,
    margin:5,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
    })
});

document.addEventListener("DOMContentLoaded", function (event) {
    
    if(document.getElementById('html')){
        var element = document.getElementById('html');
        var height = element.offsetHeight;
        if (height < screen.height) {
            document.getElementById("footer").classList.add('stikybottom');
        }}
}, false);


$(document).ready(function(){
    
    //Check to see if the window is top if not then display button
    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('.scrollToTop').fadeIn();
        } else {
            $('.scrollToTop').fadeOut();
        }
    });
    
    //Click event to scroll to top
    $('.scrollToTop').click(function(){
        $('html, body').animate({scrollTop : 0},800);
        return false;
    });
    
});





