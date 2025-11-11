fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // convertit la réponse en JSON
  .then(data => {
    // Affiche le nom du personnage dans l'élément avec id "character"
    document.querySelector('#character').textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });