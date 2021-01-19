# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:23:09 2021

@author: artur
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.widgets import Slider


fig, ax= plt.subplots()
plt.subplots_adjust(bottom=0.25)

red=np.zeros((10,10), dtype=np.int64) # Punane "kiht"
green=np.zeros((10,10), dtype=np.int64) # Roheline "kiht"
blue=np.zeros((10,10), dtype=np.int64) # Sinine "kiht"

colimg=np.array([red,green,blue]).T
graafik = ax.imshow(colimg)

# Defineerime slaideri nupud (axised)
red_slider = plt.axes([0.15, 0.15, 0.65, 0.03])
green_slider = plt.axes([0.15, 0.1, 0.65, 0.03])
blue_slider = plt.axes([0.15, 0.05, 0.65, 0.03])

# Loome Slaideri omadused

punane=Slider(red_slider,"Punane", valmin=0, valmax = 255, valinit=0, valstep=0.5)
roheline=Slider(green_slider,"Roheline", valmin=0, valmax = 255, valinit=0, valstep=0.5)
sinine=Slider(blue_slider,"Sinine", valmin=0, valmax = 255, valinit=0, valstep=0.5)

# Funktsioon graafiku uuendamiseks
def uuenda(val):
    praegune_punane=punane.val
    praegune_roheline=roheline.val
    praegune_sinine=sinine.val
    
    red= np.full((10,10), praegune_punane, dtype=np.int64)
    green=np.full((10,10), praegune_roheline, dtype=np.int64)
    blue=np.full((10,10), praegune_sinine, dtype=np.int64)
    colimg = np.array([red, green, blue]).T
    graafik.set_data(colimg)
    fig.canvas.draw()
    
punane.on_changed(uuenda)
roheline.on_changed(uuenda)
sinine.on_changed(uuenda)
