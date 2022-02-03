
window.onload = async function getqs() {
  let qsget = await eel.getqs_to_edit()();

  iner = ""

for (let i = 0; i < qsget.length; i++) {
  iner +=  `
    <div class="boxes">
  <div class="box">
      <textarea spellcheck="false" id="inputqs">${qsget[i]}</textarea>
  </div>
  <h2>: سوال ${i+1}</h2>

  </div>
  \n
  `
}
document.getElementById('boxlist').innerHTML = iner;

}


let toggle = document.querySelector('.toggle');
let menu = document.querySelector('.menu');
toggle.onclick = function () {
  menu.classList.toggle('active')
}
let textbox = document.querySelectorAll('.box');

for (const textboxs of textbox) {
  textboxs.addEventListener('click', function (event) {
    for (const vv of textbox) { vv.classList.remove('active') }
    textboxs.classList.add('active')
  })
}

let addedbox = 0;

function addtextbox() {

  addedbox = addedbox + 1;

  var boxes = document.createElement('div');
  boxes.className = "boxes";
  var box = document.createElement('div');
  box.className = "box";
  var textarea = document.createElement('textarea');
  textarea.spellcheck = false;
  textarea.id = "inputqs";
  var h2 = document.createElement('h2');
  h2.innerHTML = `: سوال ${addedbox}`;


  boxes.appendChild(box);
  box.appendChild(textarea);
  boxes.appendChild(h2);

  document.getElementById('boxlist').appendChild(boxes);




  //   document.getElementById('boxlist').innerHTML += 
  //   `
  //   <!-- ------------- -->
  // <div class="boxes">
  // <div class="box">
  //     <textarea></textarea>
  // </div>
  // <h2>: سوال ${addedbox}</h2>

  // </div>

  // <!-- ---------- -->
  //   `
  //   ;

  let textbox = document.querySelectorAll('.box');

  for (const textboxs of textbox) {
    textboxs.addEventListener('click', function (event) {
      for (const vv of textbox) { vv.classList.remove('active') }
      textboxs.classList.add('active')
    })
  }

}



function save() {

  var qsstr = "";

  var text = document.querySelectorAll("#inputqs")
  for (let step = 0; step < text.length; step++) {
    if (text[step].value == "") {
      console.log(":: Soval Khali !!!!");
    } else {
      qsstr += text[step].value + "{/_-next-qs-_`}";
    }
  }
  console.log(qsstr);


  if (qsstr == "" || qsstr == null) {
    alert("هیچ سوالی طرح نشده است")
  }
  else {

        eel.saveqsedit(qsstr);
        eel.refreashapp()
        window.location.href = "/main_page.html";
        openpageeditqs = false
        sessionStorage.setItem("openpageeditqs", openpageeditqs);
    }
  }

function goback() {

  if(confirm("ایا مایل به خروج از این قسمت هستید ")){
  window.location.href = "/main_page.html";
  openpageeditqs = false
  sessionStorage.setItem("openpageeditqs", openpageeditqs);
  }

}

async function imginsert(){

  var src = "";
  src = await eel.importimg()();
  navigator.clipboard.writeText(`<-- img_imported_cod -->${src}<-- img_imported_cod -->`)
  alert("جایی که می خواهید عکس نمایش داده شود کلیک کنید و کلید ترکیبی ctrl + v را فشار دهید")
}

function Update(){
  alert("این قسمت فعلا در نسخه بتا در دسترس نیست")
}