/*************************************************************************
 * For loading the menu.
 * The menu will not work if you open the file directly rather than on a web server.
 *************************************************************************/


(function () {
  "use strict";

  $(function () {
    var path = window.location.pathname;
    var page = path.split("/").pop();
    var baseName = page.split(".")[0];
    var menuFile = "menu_" + baseName + ".html";

    $.ajax({
      url: menuFile,
      type: 'HEAD',
      error: function () {
        // The menu file does not exist, load the default menu
        $(".menu-container").load("menu.html");
      },
      success: function () {
        // The menu file exists, load it
        $(".menu-container").load(menuFile);
      }
    });
  });
})();