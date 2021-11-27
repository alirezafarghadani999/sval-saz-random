nextqs = "" ;
numqforadd = 0;     
checkboxwordpdfinput = false 

function readq(){

     var numqst = document.getElementById("numqss").value
     var numqstf = document.getElementById("numqssfile").value
     var namef = document.getElementById("namef").value



     eel.gettext(nextqs,numqst,numqstf,namef)
 }

function zaminefile() {
    eel.zaminefile()
}

function filesavefolder() {
    eel.filesavefolder()
}

function pdf_word_input()
{
    eel.pdf_word_input()
}

function lastquse(){
    

    var hideandshow = document.getElementById("btnnextq")
    if(document.getElementById("vehicle2").checked == true){
    hideandshow.style.display = "none";
    document.getElementById("textq").style.display = "none";
    document.getElementById("vehicle1").style.marginRight= "-500px";
    document.getElementById("tbox1").style.marginRight= "-500px";
    checklastquse = true;
    
    eel.lastquse(checklastquse);
    }
    if(document.getElementById("vehicle2").checked == false){
        hideandshow.style.display = "block";
        document.getElementById("textq").style.display = "block";
        document.getElementById("vehicle1").style.marginRight= "";
        document.getElementById("tbox1").style.marginRight= "10px";
        checklastquse = false;
        eel.lastquse(checklastquse);
        document.getElementById("numqforadd").innerHTML = "تعداد سوالات اضافه شده: " + "0";
        }

}
eel.expose(numberforlastq);
function numberforlastq(n){
    document.getElementById("numqforadd").innerHTML = " تعداد سوالات اضافه شده: " + n;
}

function checkpdf(){
    var hideandshow = document.getElementById("btnnextq")
    if(document.getElementById("vehicle1").checked == true){

        document.getElementById("textq").style.display = "none";
    hideandshow.style.display = "none";
    document.getElementById("numqforadd").innerHTML = "pdf درحال استفاده از قابلیت افضودن سوال با فایل ";
    document.getElementById("pdf_wordinput").style.display = "block";
    document.getElementById("textforpdfword").innerText = "گذاشته شود <next> برای جدا کردن سوالات کافی هست بین هر سوال نشانه "
    document.getElementById("vehicle2").style.marginRight= "-500px";
    document.getElementById("tbox2").style.marginRight= "-500px";
    checkboxwordpdfinput = true;
    eel.checkboxwordpdfinput(checkboxwordpdfinput);

}

    if(document.getElementById("vehicle1").checked == false){
        document.getElementById("textq").style.display = "block";
        hideandshow.style.display = "block";
        document.getElementById("numqforadd").innerHTML = " تعداد سوالات اضافه شده: " + numqforadd;
    document.getElementById("pdf_wordinput").style.display = "none";
    document.getElementById("textforpdfword").innerText = "";
    document.getElementById("vehicle2").style.marginRight= "";
    document.getElementById("tbox2").style.marginRight= "10px";

        checkboxwordpdfinput = false;
        eel.checkboxwordpdfinput(checkboxwordpdfinput);
    }

}

function nextq(){


    var qst = document.getElementById("textq").value
    if (qst==""){
        alert("شما چیزی تایپ نکردید")
    }else{
    if (confirm("سوال زیر را تایید می کنید \n"+qst)) {
        nextqs += qst + "<__>nextq<__>"
        document.getElementById("textq").value = "";
        numqforadd = numqforadd + 1;
     document.getElementById("numqforadd").innerHTML = " تعداد سوالات اضافه شده: " + numqforadd;
    
    
      }
    }
}