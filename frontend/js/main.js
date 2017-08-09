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
  
  function showPage(pageName) {
    if (pageName === 'explorer') {
      $('#homepage').hide();
      $('#explorer').show();
    } else {
      $('#explorer').hide();
      $('#homepage').show();
    }
  }
  
  $('a[href="#!explorer"]').on('click', function() {
    showPage('explorer');
  });
  
  $('a[href="#!home"]').on('click', function() {
    showPage();
  });
  
  $('select').material_select();
  if (window.location.href.substr(-8) === 'explorer') {
    showPage('explorer');
  }
});
