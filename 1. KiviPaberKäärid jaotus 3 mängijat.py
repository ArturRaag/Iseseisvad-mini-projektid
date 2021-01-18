# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:29:40 2020

@author: artur
"""


import random
from matplotlib import pyplot as plt
from collections import Counter

valikud=["Kivi", "Paber", "Käärid"]
tulemused=[]
for i in range(1000): #Siin saad määrata katsete a
    player1_valik=random.choice(valikud)
    player2_valik=random.choice(valikud)
    player3_valik=random.choice(valikud)
    if player1_valik=="Kivi":
        if player2_valik=="Paber":
            if player3_valik=="Paber":
                tulemused.append("Viik") # NB! loogika
            elif player3_valik=="Käärid":
                tulemused.append("Viik")
            elif player3_valik=="Kivi":
                tulemused.append("Player 2")
                
        elif player2_valik=="Käärid":
            if player3_valik=="Paber":
                tulemused.append("Viik")
            elif player3_valik=="Kivi":
                tulemused.append("Viik") #NB! Loogika!
            elif player3_valik=="Käärid":
                tulemused.append("Player 1")
                
        elif player2_valik=="Kivi":
            if player3_valik=="Kivi":
                tulemused.append("Viik")
            elif player3_valik=="Paber":
                tulemused.append("Player 3")
            elif player3_valik=="Käärid":
                tulemused.append("Viik") # Siin on loogika viga, player 3 langeks välja, aga esimesed 2 jääksid viiki. Ehk player 1 ja player 2 re-rollivad?
            
    elif player1_valik== "Paber":
        if player2_valik=="Kivi":
            if player3_valik=="Kivi":
                tulemused.append("Player 1")
            elif player3_valik=="Paber":
                tulemused.append("Viik") # NB! Loogika!
            elif player3_valik=="Käärid":
                tulemused.append("Viik")
        elif player2_valik=="Käärid":
            if player3_valik=="Kivi":
                tulemused.append("Viik")
            elif player3_valik=="Käärid":
                tulemused.append("Viik") #NB! Loogika!
            elif player3_valik=="Paber":
                tulemused.append("Player 2")
        elif player2_valik=="Paber":
            if player3_valik=="Kivi":
                tulemused.append("Viik") #NB! Loogika!
            elif player3_valik=="Käärid":
                tulemused.append("Player 3")
            elif player3_valik=="Paber":
                tulemused.append("Viik")
            
    elif player1_valik=="Käärid":
        if player2_valik=="Paber":
            if player3_valik=="Kivi":
                tulemused.append("Viik")
            elif player3_valik=="Käärid":
                tulemused.append("Viik") #NB! Loogika!
            elif player3_valik=="Paber":
                tulemused.append("Player 1")
        elif player2_valik=="Kivi":
            if player3_valik=="Kivi":
                tulemused.append("Viik") #NB! Loogika!
            elif player3_valik=="Käärid":
                tulemused.append("Player 2")
            elif player3_valik=="Paber":
                tulemused.append("Viik")
        elif player2_valik=="Käärid":
            if player3_valik=="Kivi":
                tulemused.append("Player 3")
            elif player3_valik=="Käärid":
                tulemused.append("Viik") 
            elif player3_valik=="Paber":
                tulemused.append("Viik") #NB! Loogika
            
# print(tulemused)
tulemused=Counter(tulemused)
graafiku_andmed=tulemused.most_common(4)
print(graafiku_andmed)

x=[]
y=[]
for asi in graafiku_andmed:
    x.append(asi[0])
    y.append(asi[1])
plt.bar(x,y,edgecolor="black")
plt.tight_layout()
plt.show()