nextqs = "" ;
numqforadd = 0;

function readq(){

     var numqst = document.getElementById("numqss").value
     var numqstf = document.getElementById("numqssfile").value
     var namef = document.getElementById("namef").value
     var adr = document.getElementById("adr").value
     var filebaseword = document.getElementById("filebaseword").value

     eel.gettext(nextqs,numqst,numqstf,namef,adr,filebaseword)
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