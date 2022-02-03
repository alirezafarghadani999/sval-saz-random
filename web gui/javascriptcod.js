
        const list = document.querySelectorAll('.list');
        function activatelink(){
            list.forEach((item)=>
            item.classList.remove("actived"));
            this.classList.add("actived");
        }
        list.forEach((item)=>
        item.addEventListener('click',activatelink));

        setInterval(()=>{
            if(sessionStorage.getItem("openpagewritepage") == "true"){
                window.location.href = '/page/writepage/index.html'
                clearInterval()
            }

    },100)

    setInterval(()=>{
        if(sessionStorage.getItem("openpageeditqs") == "true"){
            window.location.href = '/page/editqspage/index.html';
            clearInterval();
        }

},100)
setTimeout(() => { 
document.getElementById('setting_page').contentWindow.location.reload();
},600);
