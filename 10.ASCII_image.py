# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 02:40:26 2021

@author: artur
"""

import PIL.Image

ASCII_sümbolid = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]


def resize(image, new_width=120):
    width, height= image.size
    ratio = height / width
    new_height=int(new_width*ratio)
    resized_image=image.resize((new_width, new_height))
    return (resized_image)

def grayscale(image):
    grayscale_image=image.convert("L")
    return (grayscale_image)

def image_to_ascii(image):
    pixels = image.getdata()
    characters="".join([ASCII_sümbolid[pixel//25] for pixel in pixels])
    return (characters)

def main(new_width=120):
    path=input("Sisesta pildi asukoht: \n")
    try:
        image= PIL.Image.open(path)
    except:
        print(path, " valitud asukoht ei kõlba.")
    
    new_image_data = image_to_ascii(grayscale(resize(image)))
    
    pixel_count=len(new_image_data)
    ascii_image="\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    
    print(ascii_image)
    
    with open("Tere_maailm.txt", "w") as f:
        f.write(ascii_image)

main()