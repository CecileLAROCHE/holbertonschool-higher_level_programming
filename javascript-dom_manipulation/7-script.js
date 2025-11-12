// URL de l'API
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Appel à l'API avec Fetch
fetch(url)
  // 1️⃣ On transforme la réponse en JSON
  .then(response => response.json())
  // 2️⃣ On traite les données reçues
  .then(data => {
    // Récupère l'élément <ul> dans le DOM
    const list = document.getElementById('list_movies');

    // Parcourt tous les films dans data.results
    data.results.forEach(movie => {
      // Crée un nouvel élément <li> pour chaque titre
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;

      // Ajoute l’élément à la liste <ul>
      list.appendChild(listItem);
    });
  })
  // 3️⃣ Gestion d’erreur si l’appel échoue
  .catch(error => {
    console.error('Erreur lors du chargement des films :', error);
  });
