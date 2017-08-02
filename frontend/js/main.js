$(document).ready(function(){
  $(".button-collapse").sideNav();
  
  $('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    dots: false,
    navText: ['<i class="large material-icons">chevron_left</i>', '<i class="large material-icons">chevron_right</i>'],
    responsive:{
      0:{
        items:1
      },
      600:{
        items:3
      },
      1000:{
        items:4
      }
    }
  })
});