$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.getJSON(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (e) {
    if (e.which === 13) { // Enter key
      fetchTranslation();
    }
  });
});
