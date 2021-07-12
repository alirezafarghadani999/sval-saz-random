# -*- coding: utf-8 -*-

import eel
from random import choice
import docx
from docx import Document
import os
from docx.shared import Pt


intdocx = 1
myqs = docx.Document()
qstring = ""

@eel.expose

def gettext(nextqs,numqst,numqsf,namef,adr,filebaseword):
    global qstring

    try:
        doc = docx.Document(filebaseword)  # Creating word reader object.
        data = ""
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            data = '\n'.join(fullText)
 
        print(data)
 
    except IOError:
        print('There was an error opening the file!')
        return
        
    qsnum = int(numqst)-1
    lisnumwhile = -1
    files = 1
    qs = str(nextqs).split("<__>nextq<__>")
    qs.remove("")
    numf = int(numqsf)
    numf = numf+1
    namefs = namef



    while  files < numf :
        
        myqs = docx.Document()
        myqs.add_paragraph(data+'\n')
        while qsnum > lisnumwhile :

            lisnumwhile = lisnumwhile+1
            print(qs)

            dlist = choice(qs)

            qs.remove(dlist)
            print(dlist)

            if("<~" in dlist):        
                imgs = dlist.split("<~")
                for imgsplit in imgs :
                    print(imgs)
                    if(".jpg" in imgsplit or ".png" in imgsplit):
                        print("img")
                        myqs.add_picture(imgsplit)
                    else:
                        print("________++++"+imgsplit)
                        myqs.add_paragraph(imgsplit)
                    
            else:
                myqs.add_paragraph(dlist)
            
            
            
        print("------------------------------")

        newpath = str(adr)+"\_"+str(namefs) 
        if not os.path.exists(newpath):
            os.mkdir(newpath)

        
        myqs.save(str(adr)+"/"+"_"+str(namefs)+"/" +str(namefs)+str(files) +".docx")
        files = files+1
        lisnumwhile = -1
        myqs = 0
        qs = str(nextqs).split("<__>nextq<__>")
        qs.remove("")



eel.init('web')
eel.start('main_page.html' , size=(700,500) )  # Start