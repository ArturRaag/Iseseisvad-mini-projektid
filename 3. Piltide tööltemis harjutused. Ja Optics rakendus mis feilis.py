# -*- coding: utf-8 -*-
#!/usr
"""
Created on Mon Apr 20 17:49:34 2020

@author: artur
"""

from PIL import Image
import numpy as np

def pilt1():
    size= width, height = 320, 240;
    image = Image.new( "RGB", size, "rgb(70,150,20)" )
    image.show()
    del image;

def pilt2():
    pilt=Image.open(r"C:\Users\artur\Desktop\hermann.jpg")
    pilt.show()
    
    del pilt
def pilt3():
    pilt1=Image.open(r"C:\Users\artur\Desktop\hermann.jpg")
    pilt2=Image.open(r"C:\Users\artur\Desktop\pyramid.jpg")
    
    blenditud=Image.blend(pilt1, pilt2, 0.0) #Ei tööta, sest pildi suurused ja moodid peavad samad olema.
    blenditud.show()
    del blenditud
def pilt4():
    pilt=Image.open(r"C:\Users\artur\Desktop\hermann.jpg")
    pilt.convert("L").show()

    del pilt
def pilt5():
    pilt=Image.open(r"C:\Users\artur\Desktop\hermann.jpg")
    pilt.crop((10,15,100,100)).show() #left, up, right, low
    
    del pilt
def pildi_suurus():
    pilt=Image.open(r"C:\Users\artur\Desktop\hermann.jpg")
    print(pilt.size)
    
    del pilt
def pilt7():
    pilt=Image.open(r"C:\Users\artur\Desktop\hermann.jpg")
    suurus=width,height=pilt.size
    print(pilt.getcolors(width*height)) #näitab konkreetsete toonide värvide kogust
    del pilt
def GetPixel():
    pilt=Image.open(r"C:\Users\artur\Desktop\hermann.jpg")
    suurus=width,height=pilt.size
    koordinaat=x,y=500,500
    print(pilt.getpixel(koordinaat)) #See funktsioon ütleb milline RGB värv asetseb sisestatud koordinaadil
    
    del pilt
def GetData():
    pilt=Image.open(r"C:\Users\artur\Desktop\bubble.jpg")
    suurus=width,height=pilt.size
    
    print(list(pilt.getdata()))
    
    del pilt
def Resize():
    pilt=Image.open(r"C:\Users\artur\Desktop\hermann.jpg")
    pilt.resize((50,250)).show()
    
    del pilt
def Rotate():
    pilt=Image.open(r"C:\Users\artur\Desktop\hermann.jpg")
    
    pilt.rotate(45).show()
    del pilt
def RotateWithGetData():
    pilt=Image.open(r"C:\Users\artur\Desktop\hermann.jpg")
    suurus=width,height=pilt.size
    varv_mida_otsime=(0,0,0,0)
    varv_mida_asendame=(255,255,255,255)
    rotated_image=pilt.rotate(45)
    uue_pildi_data=[]
    for varv in list(rotated_image.getdata()):
        if(varv==varv_mida_otsime):
            uue_pildi_data+=[varv_mida_asendame]
        else:
            uue_pildi_data+=[varv]
            
    uus_pilt=Image.frombuffer(pilt.mode, suurus, uue_pildi_data )
    rotated_image.putdata(uue_pildi_data)
    uus_pilt.show()
    
    
    del pilt,rotated_image
def ThinFilm():
    
    pilt=Image.open(r"C:\Users\artur\Desktop\bubble.jpg")
    suurus=width,height=pilt.size
    
    """kogun pildi kohta andmeid, leian keskmise RGB"""
    data = list(pilt.getdata())
    keskmine1=np.average(data) #võtab kõikide kanalite keskmise intensiivuse. Nii R, G kui ka B
    keskmine2=np.average(data, axis=(0)) #võtab eraldi R, G ja B kanalite keskmise
   
    """ Siin võtan indeksite kaupa tuple-st värvide toonid välja"""
    red=keskmine2[0]
    green=keskmine2[1]
    blue=keskmine2[2]
    
    """koostan värvidega listi ja seejärel tuple"""
    varvid=[]
    varvid.append(int(red))
    varvid.append(int(green))
    varvid.append(int(blue))
    
    """koostan keskmise värvitooniga sama suurusega pildi nagu originaal"""
    uus=Image.new("RGB",suurus,"rgb"+str(tuple(varvid)))
    uus.show()
    del pilt
def listimine():
    x="hi"
    y="Bye"
    list1=[]
    list1.append(y)
    list1.append(x)
    
    print(list1)
    
