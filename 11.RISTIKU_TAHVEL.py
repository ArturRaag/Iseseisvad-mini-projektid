import time
import webbrowser
import keyboard
import os
import win32api
import threading
from datetime import datetime
from datetime import date

puhke_aeg=20

def teisendus(x):
    x=x.replace("-","_")
    return x

päev = str(date.today())
päev=teisendus(päev)
extension=".txt"
faili_nimi=päev+extension

def timer():
    global aeg
    
    aeg = puhke_aeg
    while aeg !=0:
        aeg = aeg-1
        time.sleep(1)
    print("Homseni.")

webbrowser.open("https://sites.google.com/ristiku.tln.edu.ee/garderoobi/")

timer_thread = threading.Thread(target=timer)
timer_thread.start()

state_left = win32api.GetKeyState(0x01)
state_right = win32api.GetKeyState(0x02)

while True:
    new_state_left=win32api.GetKeyState(0x01)
    new_state_right=win32api.GetKeyState(0x02)
    
    if new_state_left != state_left:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("Vajutati: hiire VASAKUT nuppu. Ajahetk:", dt_string)
        with open(faili_nimi, "a") as f:
            print("Klõps: hiire VASAK. Ajahetk:",dt_string ,file=f)
        aeg=puhke_aeg
        state_left= new_state_left
        
        
    if new_state_right != state_right:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("Vajutati: hiire PAREMAT nuppu. Ajahetk:", dt_string)
        with open(faili_nimi, "a") as f:
            print("Klõps: hiire PAREM. Ajahetk:",dt_string ,file=f)
        aeg=puhke_aeg
        state_right=new_state_right
        
    if aeg ==0:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("Avalehel tagasi. Ajahetk:", dt_string)
        with open(faili_nimi, "a") as f:
            print("Avalehel tagasi. Ajahetk:",dt_string ,file=f)
        #pane kõik kinni, ava leht uuesti ning pane timer otsast peale käima.
        os.system("taskkill /im chrome.exe /f")
        webbrowser.open("https://sites.google.com/ristiku.tln.edu.ee/garderoobi/")
        timer_thread = threading.Thread(target=timer)
        timer_thread.start()
        
    if keyboard.is_pressed('q'): # if key 'q' is pressed
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('Programm katkestati! Ajahetk: ', dt_string)
        with open(faili_nimi, "a") as f:
            print("Programm katkestati! Ajahetk:",dt_string ,file=f)
        break 
        