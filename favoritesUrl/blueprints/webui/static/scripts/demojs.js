const title = document.getElementById('myh1')
const btswp = document.getElementById('btswap')

btswp.addEventListener('click', function() {
    if(title.textContent == "Texto Alterado com JavaScript"){
        title.textContent = "Texto Inicial"
    }
    else{
        title.textContent = "Texto Alterado com JavaScript"
    }
})