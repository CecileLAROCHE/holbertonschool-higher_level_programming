document.querySelector('#add_item').addEventListener('click', function() {
  const newItem = document.createElement('li'); // crée un nouvel élément <li>
  newItem.textContent = 'Item'; // définit son contenu texte
  document.querySelector('.my_list').appendChild(newItem); // l’ajoute à la liste
});