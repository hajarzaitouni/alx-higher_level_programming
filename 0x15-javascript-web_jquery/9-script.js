$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (content) {
    $('DIV#hello').text(content.hello);
  });
});
