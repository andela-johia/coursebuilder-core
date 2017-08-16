$(document).ready(function documentReady() {
  $(".button-collapse").sideNav();
  $('.collapsible').collapsible();

  $('.awards-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    dots: false,
    navText: ['<i class="ion-ios-arrow-left"></i>', '<i class="ion-ios-arrow-right"></i>'],
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 2
      },
      1000: {
        items: 4
      }
    }
  });

  $('.how-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    navText: ['<i class="ion-ios-arrow-left"></i>', '<i class="ion-ios-arrow-right"></i>'],
    items: 1
  });


  function showPage(pageName) {
    $('.page-wrapper').hide();
    $('#' + pageName).show();
  }

  var pageLinks = ['explorer', 'certification', 'homepage', 'tools', 'partners', 'feedback'];

  pageLinks.forEach(function addLinks(name) {
    $('a[href="#!' + name + '"]').on('click', function showPageEvent() {
      showPage(name);
    });

    if (window.location.href.substr(-name.length) === name) {
      showPage(name);
    }
  });

  $('select').material_select();
  
  function switchContent(divId){
    var newDiv = document.getElementById(divId);
    document.getElementById('mainContent').innerHTML = newDiv;
    $(divId).removeAttr("hidden");
  }
  
  $('.faq-switch').on('click', function(e){
    var contentDiv = '#' + $(this).data('switch');
    $('#mainContent').fadeOut(300, function(){
      $(contentDiv).fadeIn();
    });
  });
  
  $('.faq-collapsible-back').on('click', function(e){
    $(this).closest('.faq-collapsible').fadeOut(300, function(){
      $('#mainContent').fadeIn();
    });
  });
});
  

  