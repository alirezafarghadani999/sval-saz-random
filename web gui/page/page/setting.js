async function getQslist(){
    var listqs ;
   listqs = await eel.getqs()();
   showallqs(listqs)
}
function showallqs(qs){
    const listfile = qs.split("<3092480384nextfile382748372894792>")
    var htmlinnercod = '' ;
    for (let i = 0; i < listfile.length -1 ; i++) { 
        htmlinnercod += `<div class="boxqslist" ><div>${listfile[i]}</div></div>`;

    }
    document.getElementById("qsoutput").innerHTML = htmlinnercod
}
setTimeout(() => { 
    getQslist()


}, 500);

var filesrcqs = ""
var namefileqs = ""


setTimeout(() => { 
    const qsonclick = document.querySelectorAll('.boxqslist');
    function activatelink() {
        qsonclick.forEach((item) =>
            item.classList.remove("activedqs"));
        this.classList.add("activedqs");
    }
    qsonclick.forEach((item) =>
        item.addEventListener('click', activatelink));


    const selectedname = document.querySelectorAll('.boxqslist');
    function txtgiv() {
        filesrcqs = this.innerHTML.replace("<div>","").replace("</div>","");
        get_num_qs_How_much(filesrcqs)
    }
    function editqsfunc() {
        namefileqs = this.innerHTML.replace("<div>","").replace("</div>","");
        remove_and_edit(namefileqs)
    }
    selectedname.forEach((item) =>
            item.addEventListener('click', txtgiv));
    
    selectedname.forEach((item) =>
        item.addEventListener('contextmenu', editqsfunc));

    // var namefileqs = ""
    // const editqs = document.querySelectorAll('.boxqslist');
    // function editqsfunc() {
    //     namefileqs = this.innerHTML.replace("<div>","").replace("</div>","");
    //     remove_and_edit(namefileqs)
    //     console.log(namefileqs)
    // }
    // editqs.forEach((item) =>
    //     item.addEventListener('contextmenu', editqsfunc));

const rightclickfun = document.querySelectorAll('.boxqslist');
    function rightclickfunctions() {}
                      
    rightclickfun.forEach((item) =>
        item.addEventListener('contextmenu', e => { 
            rightclickfunctions()
            e.preventDefault()
        }));
},600);

var clicknum = 0;
function remove_and_edit(name){
if(clicknum == 0){
    clicknum += 1 ;
    var menutext = prompt("مایل به چه عملی روی مجموعه سوال هستید ؟ (ویرایش/حذف)")
    if( menutext == "ویرایش"){
        eel.getname_fileEdit(name)
        openpageeditqs = true
        sessionStorage.setItem("openpageeditqs", openpageeditqs);
    }else if(menutext == "حذف"){
        menutext = prompt("ایای مایل به حذف این مجموعه سوال هستید ؟(بله/خیر)")
        if (menutext == "بله"){
            eel.remove_qs(name)
            eel.refreashapp()
            alert("مجموعه سوالات حذف شد")
            location.reload();
        }

    }
    setTimeout(() => {clicknum = 0})
}
}

async function get_num_qs_How_much(str){
    var inted = 0
    inted = await eel.how_much_qs(filesrcqs)()
    document.getElementById("howmuchqs").innerHTML = `${inted} : تعداد سوالات شناسایی شده`
}

function get_output(){
    var numfile = document.getElementById("numfile").value;
    var numqs = document.getElementById("numqs").value;
    var name = document.getElementById("names").value;

    eel.output(`QS\\${filesrcqs}.sovalfile`,numfile,numqs,name)
}

function savesrc(){
    eel.where_save_do()
}

function sarbarg(){
    eel.get_sarbarg()
}

