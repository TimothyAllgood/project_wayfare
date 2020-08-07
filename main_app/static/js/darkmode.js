const darkModeBtn = document.querySelector('.dark-mode');

window.addEventListener('load', ()=>{

    if(sessionStorage.getItem('darkMode') === 'true'){
        
        document.documentElement.style.setProperty('--light', '#f1fffa');
        document.documentElement.style.setProperty('--white', 'white');
        document.documentElement.style.setProperty('--dark', '#3e5641');
    }
})

darkModeBtn.addEventListener('click', ()=>{
    if(sessionStorage.getItem('darkMode') === 'true'){
        document.documentElement.style.setProperty('--light', '#101010');
        document.documentElement.style.setProperty('--white', '#e3e3e3');
        document.documentElement.style.setProperty('--dark', '#282b28');
        sessionStorage.setItem('darkMode', 'false')
    } else{
        document.documentElement.style.setProperty('--light', '#f1fffa');
        document.documentElement.style.setProperty('--white', 'white');
        document.documentElement.style.setProperty('--dark', '#3e5641');
        sessionStorage.setItem('darkMode', 'true')
    }
    console.log(sessionStorage.getItem('darkMode'))
})



