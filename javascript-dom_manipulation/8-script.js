document.addEventListener('DOMContentLoaded', () => {
  // URL de l'API
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  // On fait la requête Fetch
  fetch(url)
    .then(response => response.json())   // Convertit la réponse en JSON
    .then(data => {
      // Récupère l'élément avec l'id 'hello'
      const helloDiv = document.getElementById('hello');

      // Affiche le texte 'hello' dans l'élément
      helloDiv.textContent = data.hello;
    })
    .catch(error => {
      console.error('Erreur lors du fetch :', error);
    });
});
