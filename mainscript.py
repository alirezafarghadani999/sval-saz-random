# -*- coding: utf-8 -*-

#اضافه کردن کتابخانه ها
import eel
from random import choice
import docx
from docx import Document
import os
import docx2txt
from docx.shared import Pt

#تعریف متغییر ها
intdocx = 1
myqs = docx.Document()
qstring = ""

#فرستادن ریکوست برای دریافت اطلاعات
@eel.expose

# دریافت اطلاعات از طریق فانکشن با جوااسکریپت
def gettext(nextqs,numqst,numqsf,namef,adr,filebaseword):
    global qstring

# دریافت سر برگ 
    try:
        doc = docx.Document(filebaseword)  
        data = ""
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            data = '\n'.join(fullText)
 
        print(data)
 
    except IOError:
        print('There was an error opening the file!')
        return
    
    # تغییر متغییر ها برای ساخت فایل ها
    qsnum = int(numqst)-1
    lisnumwhile = -1
    files = 1
    qs = str(nextqs).split("<__>nextq<__>")
    qs.remove("")
    numf = int(numqsf)
    numf = numf+1
    namefs = namef

# حلقه برای نوشتن سوالات از داخل لیست
    while  files < numf :
        
        myqs = docx.Document()
        myqs.add_paragraph(data+'\n')
        while qsnum > lisnumwhile :

            lisnumwhile = lisnumwhile+1
            print(qs)

            dlist = choice(qs)

            qs.remove(dlist)
            print(dlist)

            myqs.add_paragraph(dlist)
            
        print("------------------------------")

        newpath = str(adr)+"\_"+str(namefs) 
        if not os.path.exists(newpath):
            os.mkdir(newpath)

        # خروجی گرفتن
        myqs.save(str(adr)+"/"+"_"+str(namefs)+"/" +str(namefs)+str(files) +".docx")
        files = files+1
        lisnumwhile = -1
        myqs = 0
        qs = str(nextqs).split("<__>nextq<__>")
        qs.remove("")


# نمایش محیط گرافیکی تحت وب 
eel.init('web')
eel.start('main_page.html' , size=(700,500) )  

