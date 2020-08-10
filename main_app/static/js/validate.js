const postForm = document.getElementById('js-post-form');
const errorEl = document.querySelector('#js-post-form .error-text');
const postTitle = document.getElementById('id_title');
const postContent = document.getElementById('id_content');

const lengthCheck = (data, message) => {
	errorMsg = {
		isValid: true,
		msg: '',
	};
	if (data.value.length < 1) {
		errorMsg.isValid = false;
		errorMsg.msg = `${message} is required`;
	} else if (data.value.length > 200 && data.name === 'title') {
		errorMsg.isValid = false;
		errorMsg.msg = `${message} cannot contain more than 200 characters`;
	} else if (data.value.length > 999 && data.name == 'content') {
		errorMsg.isValid = false;
		errorMsg.msg = `${message} cannot contain more than 1000 characters`;
	}
	return errorMsg;
};

postForm.addEventListener('submit', (e) => {
	let titleCheck = lengthCheck(postTitle, 'Title');
	let contentCheck = lengthCheck(postContent, 'Content');
	if (!titleCheck.isValid) {
		e.preventDefault();
		errorEl.textContent = titleCheck.msg;
	}

	if (!contentCheck.isValid) {
		e.preventDefault();
		errorEl.textContent = contentCheck.msg;
	}
});
