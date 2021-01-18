# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:40:31 2021

@author: artur
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



# Meie funktsioon
x=np.linspace(-5,5,100)
tous= 1
vabaliige=0
funktsioon=tous*x+vabaliige

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
graafik, = ax.plot(x,funktsioon)
ax.set_title("Funktsiooni y=ax+b graafik")

# Defineerime Slider'i nuppu.
tous_slider = plt.axes([0.15, 0.1, 0.65, 0.03]) # x-position, y-position, width and height
vabaliikme_slider = plt.axes([0.15, 0.05, 0.65, 0.03])

# Slider'i omadused
graafiku_tous = Slider(tous_slider, "Tõus", valmin=-10, valmax=10, valinit=0, valstep=(0.1))
graafiku_vabaliige = Slider(vabaliikme_slider, "Vabaliige", valmin=-5, valmax=5, valinit=0, valstep=0.1)

# Siin saab jaotiste väärtusi muuta omal soovil. np.arange(algus, lõpp, samm)
ax.set_xticks(np.arange(min(x), max(x), 1))
ax.set_yticks(np.arange(min(funktsioon),max(funktsioon),1))
ax.grid(True)

# Loome ka funktsiooni teksti mida graafikule display'ida.
graafiline_text=("y="+str(tous)+"x"+"+"+str(vabaliige))
tekst_joonisel=ax.text(3,-4, graafiline_text, fontsize=14)

# Funktsiooni (graafiku) uuendamine.
def uuenda(val):
    praegune_tous = graafiku_tous.val
    praegune_vabaliige=graafiku_vabaliige.val
    funktsioon=praegune_tous*x+praegune_vabaliige
    graafik.set_ydata(funktsioon)
    graafiline_text=("y="+str(round(praegune_tous,1))+"x"+"+"+"("+str(round(praegune_vabaliige,1))+")")
    tekst_joonisel.set_text(graafiline_text)
    fig.canvas.draw() # redraws the figure
    
graafiku_tous.on_changed(uuenda)
graafiku_vabaliige.on_changed(uuenda)

plt.show()


