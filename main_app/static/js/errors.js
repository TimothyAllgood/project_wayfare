$('#signupModal').modal('show');

const postForm = document.getElementById('js-post-form');
const errorEl = document.querySelector('#js-post-form .error-text');
const postTitle = document.getElementById('id_title');
const postContent = document.getElementById('id_content');

const lengthCheck = (data) => {
	errorMsg = {
		isValid: true,
		msg: '',
	};
	if (data.length < 1) {
		errorMsg.isValid = false;
		errorMsg.msg = 'Title must be between 1 and 200 characters';
	} else if (data.length > 200) {
		errorMsg.isValid = false;
		errorMsg.msg = 'Title must be between 1 and 200 characters';
	}
	return errorMsg;
};

postForm.addEventListener('change', (e) => {
	console.log(postTitle.value.length);
});

postForm.addEventListener('submit', (e) => {
	let titleCheck = lengthCheck(postTitle.value);
	let contentCheck = lengthCheck(postContent.value);
	if (!titleCheck.isValid) {
		e.preventDefault();
		errorEl.textContent = titleCheck.msg;
	}

	if (!contentCheck.isValid) {
		e.preventDefault();
		errorEl.textContent = contentCheck.msg;
	}
});
