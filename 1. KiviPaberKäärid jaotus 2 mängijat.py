# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:21:41 2020

@author: artur
"""

import random  
from matplotlib import pyplot as plt
from collections import Counter

valikud=["Kivi", "Paber", "Käärid"]
tulemused=[]
for i in range(1000): # Siin saad määrata katsete arvu.
    player1_valik=random.choice(valikud)
    player2_valik=random.choice(valikud)
    
    if player1_valik=="Kivi":
        if player2_valik=="Paber":
            tulemused.append("Player 2")
        elif player2_valik=="Käärid":
            tulemused.append("Player 1")
        elif player2_valik==player1_valik: #Võib ka lihtsalt lõpetada else käsuga. Aga ei ole soovituslik
            tulemused.append("Viik")
            
    elif player1_valik== "Paber":
        if player2_valik=="Kivi":
            tulemused.append("Player 1")
        elif player2_valik=="Käärid":
            tulemused.append("Player 2")
        else:
            tulemused.append("Viik")
            
    elif player1_valik=="Käärid":
        if player2_valik=="Paber":
            tulemused.append("Player 1")
        elif player2_valik=="Kivi":
            tulemused.append("Player 2")
        else:
            tulemused.append("Viik")
            
# print(tulemused)
tulemused=Counter(tulemused)
graafiku_andmed=tulemused.most_common(3)
print(graafiku_andmed)

x=[]
y=[]
for asi in graafiku_andmed:
    x.append(asi[0])
    y.append(asi[1])
plt.bar(x,y,edgecolor="black")
plt.tight_layout()
plt.show()    
    
    

# Sama asi aga lihtsalt teksti kujul ja graafikut pole.

def KiviPaberKäärid_text_kuju():
    
    from matplotlib import pyplot as plt
    from collections import Counter
    

    valikud=["Kivi", "Paber", "Käärid"]
    
    for i in range(10):
        player1_valik=random.choice(valikud)
        player2_valik=random.choice(valikud)
        
        if player1_valik=="Kivi":
            if player2_valik=="Paber":
                print("Mängija 2 võitis!")
            elif player2_valik=="Käärid":
                print("Mängija 1 võitis!")
            elif player2_valik==player1_valik: #Võib ka lihtsalt lõpetada else käsuga.
                print("1. Jäite viiki!")
                
        elif player1_valik== "Paber":
            if player2_valik=="Kivi":
                print("Mängija 1 võitis!")
            elif player2_valik=="Käärid":
                print("Mängija 2 võitis!")
            else:
                print("2. Jäite viiki!")
                
        elif player1_valik=="Käärid":
            if player2_valik=="Paber":
                print("Mängija 1 võitis!")
            elif player2_valik=="Kivi":
                print("Mängija 2 võitis!")
            else:
                print("3. Jäite viiki!")