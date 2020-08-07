const bio = document.querySelector('.bio');
const bioForm = document.querySelector('.bio-form textarea');

bioForm.style.height = bio.clientHeight + 10 + 'px';
bioForm.value = bio.textContent.trim();
