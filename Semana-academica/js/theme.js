/////////////////////////////////////////////////////////////////////
// jQuery for page scrolling feature - requires jQuery Easing plugin
/////////////////////////////////////////////////////////////////////

$('.page-scroll').bind('click', function(event) {
    var $anchor = $(this);
    $('html, body').stop().animate({
        scrollTop: $($anchor.attr('href')).offset().top -64
    }, 1500, 'easeInOutExpo');
    event.preventDefault();
});



////////////////////////////////////////////////////////////////////////
// On-Scroll Animated Header: https://github.com/codrops/AnimatedHeader
////////////////////////////////////////////////////////////////////////

var cbpAnimatedHeader = (function() {

    var docElem = document.documentElement,
        header = document.querySelector( '.navbar-fixed-top' ),
        didScroll = false,
        changeHeaderOn = 10;

    function init() {
        window.addEventListener( 'scroll', function( event ) {
            if( !didScroll ) {
                didScroll = true;
                setTimeout( scrollPage, 250 );
            }
        }, false );
    }

    function scrollPage() {
        var sy = scrollY();
        if ( sy >= changeHeaderOn ) {
            classie.add( header, 'navbar-shrink' );
        }
        else {
            classie.remove( header, 'navbar-shrink' );
        }
        didScroll = false;
    }

    function scrollY() {
        return window.pageYOffset || docElem.scrollTop;
    }

    init();

})();



//////////////////////////////////////////////
// Highlight the top nav as scrolling occurs
//////////////////////////////////////////////

$('body').scrollspy({
    target: '.navbar',
    offset: 65
})



///////////////////////////////////////////
// Display loading image while page loads
///////////////////////////////////////////

// Wait for window load
$(window).load(function() {
    // Animate loader off screen
    $(".page-loader").fadeOut("slow");
});



////////////////////
// Top sliding bar
////////////////////

var megaDrop = $('.top-slidingbar-trigger');
var megaContainer = $('#top-slidingbar');
 
$(megaDrop).click(function() {
    $(megaContainer).slideToggle(300,function(){
        if ($(this).is(":hidden")) $(megaDrop).html("+");
        else $(megaDrop).html("×");
    });
});



////////////////////////////////////////////////////
// OWL Carousel: http://owlgraphic.com/owlcarousel
////////////////////////////////////////////////////

// Intro text carousel
$("#owl-intro-text").owlCarousel({
    singleItem : true,
    autoPlay : 9000,
    stopOnHover : true,
    navigation : false,
    navigationText : false,
    pagination : false
})

// Blog (Latest News) carousel for boxed layout
$("body.boxed #owl-blog").owlCarousel({
    items : 3,
    itemsDesktop : [1199,3],
    itemsDesktopSmall : [980,2],
    itemsTablet: [768,1],
    autoPlay : 9000,
    stopOnHover : true,
    pagination : false
})

// Blog (Latest News) carousel for full width layout
$("#owl-blog").owlCarousel({
    items : 4,
    itemsDesktop : [1199,3],
    itemsDesktopSmall : [980,2],
    itemsTablet: [768,1],
    autoPlay : 9000,
    stopOnHover : true,
    pagination : false
})

// Trusted by carousel
$("#owl-trusted-by").owlCarousel({
    items : 4,
    itemsDesktop : [1199,3],
    itemsDesktopSmall : [980,2],
    itemsTablet: [768,1],
    autoPlay : 5000,
    stopOnHover : true,
    pagination : false
})

// Testimonials carousel
$("#owl-testimonial").owlCarousel({
    singleItem : true,
    pagination : true,
    autoHeight : true
})

// Portfolio modal carousel
$(".owl-portfolio-modal").owlCarousel({
    singleItem : true,
    pagination : true
})



////////////////////////////////////////////////////////////////////
// Stellar (parallax): https://github.com/markdalgleish/stellar.js
////////////////////////////////////////////////////////////////////

$.stellar({
    // Set scrolling to be in either one or both directions
    horizontalScrolling: false,
    verticalScrolling: true,
});



///////////////////////////////////////////////////////////
// WOW animation scroll: https://github.com/matthieua/WOW
///////////////////////////////////////////////////////////

new WOW().init();



////////////
// Tooltip
////////////

$('[data-toggle="tooltip"]').tooltip()



////////////////////////////////////////////////////////////////////////////////////////////
// Counter-Up (requires jQuery waypoints.js plugin): https://github.com/bfintal/Counter-Up
////////////////////////////////////////////////////////////////////////////////////////////

$('.counter').counterUp({
    delay: 10,
    time: 2000
});



/////////////////////////////////////////////////
// Typed: https://github.com/mattboldt/typed.js
/////////////////////////////////////////////////

// featured box typed text
$(".featured-box .typed-element").typed({

    strings: ["Pure^3000", "Total^3000", "Brutal^3000"], // Waits 3000ms after typing word        
    typeSpeed: 100, // typing speed        
    startDelay: 0, // time before typing starts        
    loop: true, // loop        
    showCursor: false, // show cursor
    cursorChar: "|" // character for cursor
    
});

// Video intro typed text
$("#video-intro-section .typed-element").typed({

    strings: ["Awesome^3000", "^1000Brilliant^3000", "^1000Incredible^3000", "^1000Priceless^3000", "^1000Responsive^3000"], // Waits 3000ms after typing word        
    typeSpeed: 100, // typing speed        
    startDelay: 2000, // time before typing starts        
    loop: true, // loop        
    showCursor: true, // show cursor
    cursorChar: "|" // character for cursor

});



/////////////////////////
// Scroll to top button
/////////////////////////

// Check to see if the window is top if not then display button
$(window).scroll(function(){
    if ($(this).scrollTop() > 100) {
        $('.scrolltotop').fadeIn();
    } else {
        $('.scrolltotop').fadeOut();
    }
});

// Click event to scroll to top
$('.scrolltotop').click(function(){
    $('html, body').animate({scrollTop : 0}, 1500, 'easeInOutExpo');
    return false;
});



////////////////////////////////////////////////////////////////////
// Close mobile menu when click menu link (Bootstrap default menu)
////////////////////////////////////////////////////////////////////

$(document).on('click','.navbar-collapse.in',function(e) {
    if( $(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle' ) {
        $(this).collapse('hide');
    }
});