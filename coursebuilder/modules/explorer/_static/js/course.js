$(document).ready(function documentReady() {
  $(".button-collapse").sideNav();
  $("select").material_select();
  $(".dropdown-button").dropdown();

  $(".course-carousel").owlCarousel({
    loop: false,
    margin: 10,
    nav: true,
    navText: [
      '<i class="material-icons small">chevron_left</i>',
      '<i class="material-icons small">chevron_right</i>'
    ],
    items: 1
  });

  $(".course-carousel").on("changed.owl.carousel", function(event) {
    var changed_carousel = $(event.target).closest(".course-carousel");
    var position_coordinates = changed_carousel.position();
    window.scrollTo({
      behavior: "smooth",
      left: position_coordinates.left,
      top: position_coordinates.top
    });
  });

  var sidebarToggle = false;
  $("body").on("click", "#hideCourseSidenav", function() {
    sidebarToggle = !sidebarToggle;
    var sidebarWidth = sidebarToggle ? $(".course-accordion").width() : 0;

    $(".course-accordion").toggleClass("hide-sidenav");
    $(".course-card").animate({ "margin-left": sidebarWidth / 2 + "px" }, 300);
    $(".course-accordion").animate(
      { "margin-left": "-" + sidebarWidth + "px" },
      300
    );
  });

  $(".course-accordion .collapsible").clone().appendTo("#courseMobileSidebar");
  $(".collapsible").collapsible();
  $("body").on("click", "#closeSideNav", function() {
    $(".button-collapse").sideNav("hide");
  });

  /**
   * This function returns the first element within the selector that matches
   * the specified selector
   * @param {string} element
   * @returns {any} - the first element
   */
  function getQueryElement(element) {
    if (typeof element == "string") {
      return document.querySelector(element);
    }
    return element;
  }
  $(".course-carousel").on("click", function (event) {
    $(document.documentElement).off("keydown");
    var queryElement = getQueryElement(":focus");
    var owlCarousel = $(event.target).closest(".owl-carousel");
    $(document.documentElement).on("keydown", function (event) {
      if (queryElement === null) {
        if (event.keyCode == 37) {
          owlCarousel.trigger("prev.owl.carousel");
        } else if (event.keyCode == 39) {
          owlCarousel.trigger("next.owl.carousel");
        }
      }
    });
  });
});
