const userCity = document.querySelector('.user-city').textContent;
const citySelect = document.getElementById('id_city');

document.querySelector("#id_avatar").required = false;

citySelect.value = userCity;
