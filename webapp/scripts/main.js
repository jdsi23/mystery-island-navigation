// main.js
function closePopup() {
  document.getElementById('info-popup').classList.add('hidden');
  document.getElementById('popup-title').textContent = '';
  document.getElementById('popup-description').textContent = '';
  document.getElementById('popup-image').src = '';
}

document.addEventListener('keydown', function (event) {
  if (event.key === 'Escape') {
    closePopup();
  }
});
