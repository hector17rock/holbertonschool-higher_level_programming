fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    documnet.querySelector('#character').textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching character:', error);
  });
