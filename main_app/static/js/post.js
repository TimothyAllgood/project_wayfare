const postsMenus = document.querySelectorAll('.posts-list-items');
const postNext = document.querySelector('.post-btn');
const postPrevious = document.querySelector('.previous-post-btn');

postsMenus[0].classList.add('active-post-list');

let k = 0;
postPrevious.style.display = 'none'


postNext.addEventListener('click', (e)=>{
	postPrevious.style.display = 'initial'
	postsMenus[k].classList.remove('active-post-list')
	k++;
	postsMenus[k].classList.add('active-post-list')
	if(k == postsMenus.length-1){
		e.target.style.display='none'
	}	
})

postPrevious.addEventListener('click', (e)=>{
    postNext.style.display = 'initial'
    postsMenus[k].classList.remove('active-post-list')
    k--;
    postsMenus[k].classList.add('active-post-list')
    if(k == 0){
        e.target.style.display='none'
    }
})