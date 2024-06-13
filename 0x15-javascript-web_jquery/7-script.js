$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $.each(data, function (key, val) {
    if (key === 'name') {
      $('#character').text(val);
    }
  });
});
