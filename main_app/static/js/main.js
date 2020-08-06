if (document.querySelector('.user-city')) {
	const userCity = document.querySelector('.user-city').textContent;
	const citySelect = document.getElementById('id_city');
	citySelect.value = userCity;
}

document.querySelector('#id_avatar').required = false;
