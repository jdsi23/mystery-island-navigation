// map.js
fetch('data/attractions.json')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('attraction-icons');

    data.forEach(attraction => {
      const icon = document.createElement('img');
      icon.src = `assets/icons/${attraction.icon}`;
      icon.alt = attraction.name;
      icon.classList.add('attraction-icon');

      icon.style.left = attraction.mapX || '50%';
      icon.style.top = attraction.mapY || '50%';

      icon.addEventListener('click', () => {
        document.getElementById('popup-title').textContent = attraction.name;
        document.getElementById('popup-description').textContent = attraction.description;
        document.getElementById('popup-image').src = `assets/images/${attraction.image}`;
        document.getElementById('info-popup').classList.remove('hidden');
      });

      container.appendChild(icon);
    });
  })
  .catch(error => console.error('Error loading attractions:', error));
