$(document).ready(function documentReady() {
  $(".button-collapse").sideNav();
  $('select').material_select();
  $('.dropdown-button').dropdown();

  $('.course-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    navText: ['<i class="material-icons small">chevron_left</i>', '<i class="material-icons small">chevron_right</i>'],
    items: 1
  });
});
