# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 02:01:51 2021

@author: artur
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


# Suvaline Parabooli taoline funktsioon

x_algus=-3
x_lõpp=3

x=np.linspace(x_algus, x_lõpp, 1000)
fx=x**2-5

praegune_puutuja=0
praegune_y=praegune_puutuja**2-5

fig,ax = plt.subplots()
plt.style.use('default')

# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))
# Hide the top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.plot(1,0,">k",transform=ax.get_yaxis_transform(),clip_on=False)
ax.plot(0,1,"^k",transform=ax.get_xaxis_transform(),clip_on=False)

plt.subplots_adjust(bottom=0.25)
ax.plot(x,fx,"b") # See on joonis, mis jääb muutumatuks/ WILL NOT UPDATE
graafik1, = ax.plot(x,fx) # this plot WILL UPDATE later on
graafik2, =ax.plot(0,-5,"ro")
ax.set_title("Funktsiooni f(x) graafik, koos puutujaga", fontsize= 16)

# Siin saab jaotiste väärtusi muuta omal soovil. np.arange(algus, lõpp, samm)
ax.set_xticks(np.arange(min(x), max(x), 1))
ax.set_yticks(np.arange(min(fx),max(fx),1))
ax.grid(True)



# Defineerime Slider'i nuppu.
puutuja_slider = plt.axes([0.15, 0.1, 0.65, 0.03]) # x-position, y-position, width and height

# Slider'i omadused
puutuja = Slider(puutuja_slider, "X:", valmin=x_algus, valmax=x_lõpp, valinit=praegune_puutuja, valstep=(0.1))

# Loome ka funktsiooni teksti mida graafikule display'ida.
graafiline_text=("P("+str(round(praegune_puutuja,1))+","+ str(round(praegune_y,1))+ ")")
tekst_joonisel=ax.text(0.5,-5.5, graafiline_text, fontsize=12)


# Funktsiooni (graafiku) uuendamine.
def uuenda(val):
    praegune_puutuja = puutuja.val
    puutuja_joonisel=(praegune_puutuja**2-5)+(2*praegune_puutuja)*(x-praegune_puutuja)
    praegune_y=praegune_puutuja**2-5
   
    graafik1.set_ydata(puutuja_joonisel)
    graafik2.set_data(praegune_puutuja,praegune_y)
    graafiline_text=("P("+str(round(praegune_puutuja,1))+","+ str(round(praegune_y,1))+ ")")
    tekst_joonisel.set_text(graafiline_text)
    tekst_joonisel.set_x(praegune_puutuja+0.5)
    tekst_joonisel.set_y(praegune_y-0.5)
    fig.canvas.draw() # redraws the figure

    
puutuja.on_changed(uuenda)
plt.show()