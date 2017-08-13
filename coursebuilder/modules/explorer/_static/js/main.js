$(document).ready(function () {
  $(".button-collapse").sideNav();

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

  pageLinks.forEach(function (name) {
    $('a[href="#!' + name + '"]').on('click', function () {
      showPage(name);
    });

    if (window.location.href.substr(-name.length) === name) {
      showPage(name);
    }
  });

  $('select').material_select();
});
