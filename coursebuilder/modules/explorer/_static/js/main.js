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
        $('.page-wrapper').hide();
        $('#' + pageName).show();
    }

    $('a[href="#!explorer"]').on('click', function () {
        showPage('explorer');
    });

    $('a[href="#!certification"]').on('click', function () {
        showPage('certification');
    });

    $('a[href="#!homepage"], a[href="#!home"]').on('click', function () {
        showPage('homepage');
    });

    $('a[href="#!tools"]').on('click', function () {
        showPage('tools');
    });
  

    $('select').material_select();

    if (window.location.href.substr(-8) === 'explorer') {
        showPage('explorer');
    }
});
