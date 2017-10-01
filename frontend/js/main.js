$(document).ready(function () {
  $('.button-collapse').sideNav();
  $('.dropdown-button').dropdown();
  $('ul.tabs').tabs();
  $('.collapsible').collapsible();

  $('.slider-carousel').owlCarousel({
    loop: true,
    margin: 10,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: false,
    dots: false,
    items: 1
  });

  $('.awards-carousel').owlCarousel({
    loop: true,
    margin: 10,
    autoplay: true,
    autoplayTimeout: 1000,
    autoplayHoverPause: false,
    dots: false,
    items: 4
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
    $('.nav-link').removeClass('active-link');
    $('.home-main-menu a[href="#!' + pageName + '"]').addClass('active-link');
  }

  var pageLinks = ['explorer', 'certification', 'homepage', 'tools', 'partners', 'feedback', 'faqs', 'events'];

  pageLinks.forEach(function (name) {
    $('a[href="#!' + name + '"]').on('click', function () {
      showPage(name);
    });

    if (window.location.href.substr(-name.length) === name) {
      showPage(name);
    }
  });

  $('select').material_select();

  $('.faq-switch').on('click', function (e) {
    $('#mainContent').fadeOut(300, function () {
      $('#' + $(e.target).data('switch')).fadeIn();
    });
  });

  $('.faq-collapsible-back').on('click', function (e) {
    $(e.target).closest('.faq-collapsible').fadeOut(300, function () {
      $('#mainContent').fadeIn();
    });
  });

  var sidebarToggle = false;
  $('body').on('click', '#hideCourseSidenav', function () {
    sidebarToggle = !sidebarToggle;
    var sidebarWidth = sidebarToggle ? $('.course-accordion').width() : 0;

    $('.course-accordion').toggleClass('hide-sidenav');
    $('.course-card').animate({ 'margin-left': sidebarWidth / 2 + 'px' }, 300);
    $('.course-accordion').animate({ 'margin-left': '-' + sidebarWidth + 'px' }, 300);
  });
});