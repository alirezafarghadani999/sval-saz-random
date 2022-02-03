import os , glob
import tkinter as tk
from tkinter import filedialog
from tkinter.constants import S
import eel
import docx
import pdfplumber
from prosses import prossesqs
from getdata_server import server

version_application = "v4.0beta"

listfileqs =""
for file in glob.glob("QS/*.sovalfile"):
    listfileqs+=file.replace('QS\\',"").replace(".sovalfile","")+"<3092480384nextfile382748372894792>"


@eel.expose
def getdata_server_home():
    global version_application
    data = server.get_home_data(version_application)

    return data

# __________________________________________


@eel.expose

def saveqs(qsstr,namesave):
    try:
        os.makedirs("QS")
    except:
        pass
    with open("QS/"+namesave+".sovalfile","+a" ,encoding="utf-8") as filesave :
        filesave.write(qsstr)
        
@eel.expose
def importimg():
    root = tk.Tk()
    root.withdraw()
    imgsrc = filedialog.askopenfilename(title="وارد کردن عکس",
    filetypes=[('عکس', '.jpg'),('عکس', '.png')])
    return imgsrc

@eel.expose
def refreashapp():
    global listfileqs
    listfileqs = ""
    for file in glob.glob("QS/*.sovalfile"):
        listfileqs+=file.replace('QS\\',"").replace(".sovalfile","")+"<3092480384nextfile382748372894792>"

@eel.expose
def getqs():
    global listfileqs
    return listfileqs


#_______________________________________________


where_save = ""
sarbarg = ""

@eel.expose
def output(filesrc,numberfile,numberqs,name):
    global where_save , sarbarg
    if filesrc != "QS\\.sovalfile" and numberfile != "" and numberqs != "" and name != "" and where_save != "":
        prossesqs.output_ps(filesrc,numberfile,numberqs,name,sarbarg,where_save)

@eel.expose
def where_save_do():
    global where_save , sarbarg
    root = tk.Tk()
    root.withdraw()
    where_save = filedialog.askdirectory()



@eel.expose
def get_sarbarg():
    global where_save , sarbarg
    root = tk.Tk()
    root.withdraw()
    sarbarg = filedialog.askopenfilename(title="فایل سربرگ",
    filetypes=[(' word وارد کردن سربرگ با فرمت ', '.docx')])

@eel.expose
def how_much_qs(str):
    with open(f"QS\\{str}.sovalfile" , "r+", encoding="utf-8") as sqfile:
            textsq = sqfile.read()

    textsq = textsq.split("{/_-next-qs-_`}")
    textsq.remove('')
    return len(textsq)


#--------------------------------------------------------------------------

@eel.expose
def remove_qs(name):
    os.remove(f"QS\\{name}.sovalfile")
    

@eel.expose
def import_sovalsaz():
    root = tk.Tk()
    root.withdraw()
    sovalsaz = filedialog.askopenfilename(title="ورودی سوالات از طریق فایل",
    filetypes=[('وارد کردن فایل سوال ساز', '.sovalfile')])
    prossesqs.import_sovalsazfile(sovalsaz)
    
edit_file_src=""
@eel.expose
def getname_fileEdit(src):
    global edit_file_src
    edit_file_src = src

@eel.expose
def getqs_to_edit():
    global edit_file_src
    with open(f"QS\\{edit_file_src}.sovalfile" , "r+", encoding="utf-8") as sqfile:
        textsq = sqfile.read()

    textsq = textsq.split("{/_-next-qs-_`}")
    textsq.remove('')

    return textsq

@eel.expose
def saveqsedit(qsstr):
    global edit_file_src
    os.remove(f"QS\\{edit_file_src}.sovalfile")
    try:
        os.makedirs("QS")
    except:
        pass
    with open("QS/"+edit_file_src+".sovalfile","+a" ,encoding="utf-8") as filesave :
        filesave.write(qsstr)

eel.init("web gui")
eel.start('main_page.html',size=(1124, 868) ) # Start

                             