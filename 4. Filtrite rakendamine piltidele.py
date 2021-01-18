# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 05:48:53 2020

@author: artur
"""

from PIL import Image, ImageFilter
import PIL.ImageOps

image = Image.open('test.jpg')
display(image)


# define a kernel (filter)
# 1st argument: kernel size
# 2nd argument: kernel definition
kernel = ImageFilter.Kernel((3, 3), (0, -1, 0, -1, 5, -1, 0, -1, 0))

# filter the image using the defined kernel, it should sharpen it a bit
sharp_img = image.filter(kernel)
# display(sharp_img)


# now lets blur the bee back using approximate Gaussian blur
# 16 is a scale factor, so the kernel is the same as
# kernel = ImageFilter.Kernel((3,3), (1/16, 2/16, 1/16, 2/16, 4/16, 2/16, 1/16, 2/16, 1/16))
kernel = ImageFilter.Kernel((3,3), (1, 2, 1, 2, 4, 2, 1, 2, 1), 16)
blurred_img = sharp_img.filter(kernel)
# display(blurred_img)



# TODO: apply 3 by 3 edge detection kernel by modifing the kernel = .. definition
# e.g:
# [ -1 -1 -1 ]
# [ -1  7 -1 ]
# [ -1 -1 -1 ]
# (see previous kernels for an example)


kernel = ImageFilter.Kernel((3,3), (-1, -1, -1, -1, 7, -1, -1, -1, -1)) # See annab musta pildi millegipärast?

# kernel = ImageFilter.Kernel((3,3), (1, 2, 1, 2, 4, 2, 1, 2, 1), 16)

# 5x5 gaussian blur ((5,5), (1,4,6,4,1,4,16,24,16,4,6,24,36,24,6,4,16,24,16,4,1,4,6,4,1), 256)

# all is fine below here, no modification needed
# convert to grayscale for easier implementation
gray_img = image.convert("L")
edge_img = gray_img.filter(kernel)
display(edge_img)




