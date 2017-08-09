$(document).ready(function(){
  $(".button-collapse").sideNav();
  
  $('.awards-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    dots: false,
    navText: ['<i class="ion-ios-arrow-left"></i>', '<i class="ion-ios-arrow-right"></i>'],
    responsive:{
      0:{
        items:1
      },
      600:{
        items:2
      },
      1000:{
        items:4
      }
    }
  });
  
  $('.how-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    navText: ['<i class="ion-ios-arrow-left"></i>', '<i class="ion-ios-arrow-right"></i>'],
    items: 1,
  });
  
  $('a[href="#!explorer"]').on('click', function() {
    $('#homepage').hide();
    $('#explorer').show();
    $('#certification').hide();
  });
  
  $('a[href="#!home"]').on('click', function() {
    $('#explorer').hide();
    $('#homepage').show();
    $('#certification').hide();
  });

  $('a[href="#!certification"]').on('click', function() {
    $('#explorer').hide();
    $('#homepage').hide();
    $('#certification').show();
  });
  
  $('select').material_select();
  
});
