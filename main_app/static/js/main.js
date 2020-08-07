if (document.querySelector('.user-city')) {
	const userCity = document.querySelector('.user-city').textContent;
	const citySelect = document.getElementById('id_city');
	citySelect.value = userCity;
}

if(document.querySelector('#id_avatar')){
	document.querySelector('#id_avatar').required = false;
}

const posts = document.querySelectorAll('.post-page');
const next = document.querySelector('.next');
const previous = document.querySelector('.previous');
const pageCounter = document.querySelector('.page-counter');

// Second Pagination
const cityPosts = document.querySelectorAll('.city-post-page');
const cityNext = document.querySelector('.city-next');
const cityPrevious = document.querySelector('.city-previous');
const cityPageCounter = document.querySelector('.city-page-counter');

for(let i = 0; i < posts.length; i++){
	pageCounter.insertAdjacentHTML('beforeend', `<a href="#">${i+1}</a>`)
}

previous.style.display = 'none'

posts[0].classList.add('active-page');
let i = 0;
next.addEventListener('click', (e)=>{
	previous.style.display = 'flex'
	posts[i].classList.remove('active-page')
	i++;
	posts[i].classList.add('active-page')
	if(i == posts.length-1){
		e.target.style.display='none'
	}	
})

previous.addEventListener('click', (e)=>{
		next.style.display = 'flex'
		posts[i].classList.remove('active-page')
		i--;
		posts[i].classList.add('active-page')
		if(i == 0){
			e.target.style.display='none'
		}
})

pageCounter.addEventListener('click', (e)=>{
	for(post of posts){
		post.classList.remove('active-page')
	}
	i = parseInt(e.target.textContent);
	next.style.display='flex'
	previous.style.display='flex'
	if(i == posts.length){
		next.style.display='none'
	} 
	if (i-1==0){
		previous.style.display='none'
	} 
	i = parseInt(e.target.textContent)-1;
	posts[parseInt(e.target.textContent)-1].classList.add('active-page')
})


// City
for(let i = 0; i < posts.length; i++){
	cityPageCounter.insertAdjacentHTML('beforeend', `<a href="#">${i+1}</a>`)
}

cityPrevious.style.display = 'none'

cityPosts[0].classList.add('active-page');
let j = 0;
cityNext.addEventListener('click', (e)=>{
	cityPrevious.style.display = 'flex'
	cityPosts[j].classList.remove('active-page')
	j++;
	cityPosts[j].classList.add('active-page')
	if(j == cityPosts.length-1){
		e.target.style.display='none'
	}	
})

cityPrevious.addEventListener('click', (e)=>{
		cityNext.style.display = 'flex'
		cityPosts[j].classList.remove('active-page')
		j--;
		cityPosts[j].classList.add('active-page')
		if(j == 0){
			e.target.style.display='none'
		}
})

cityPageCounter.addEventListener('click', (e)=>{
	for(post of cityPosts){
		post.classList.remove('active-page')
	}
	j = parseInt(e.target.textContent);
	cityNext.style.display='flex'
	cityPrevious.style.display='flex'
	if(j == cityPosts.length){
		cityNext.style.display='none'
	} 
	if (j-1==0){
		cityPrevious.style.display='none'
	} 
	j = parseInt(e.target.textContent)-1;
	cityPosts[parseInt(e.target.textContent)-1].classList.add('active-page')
})




