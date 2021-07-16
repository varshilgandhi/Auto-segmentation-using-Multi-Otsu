# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 18:45:36 2021

@author: abc
"""

import matplotlib.pyplot as plt
import numpy as np

from skimage import data, io, img_as_ubyte
from skimage.filters import threshold_multiotsu

#Read an image
image = io.imread("BSE.jpg")

#show our image
plt.imshow(image, cmap="gray")

#Apply Multi-Otsu filter
thresholds = threshold_multiotsu(image, classes=5)

#Let's segment our thresholds into multiple classes using digitize function of numpy
regions = np.digitize(image, bins=thresholds)

#Let's convert our image from int64 to int8
output = img_as_ubyte(regions)

#save our image
plt.imsave("Otsu_Segmented.jpg", output)

#Let's show and plot our images

#Let us look at the input image, thresholds on the histogram and final segmented
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 3.5))

#Plotting the original image
ax[0].imshow(image, cmap="gray")
ax[0].set_title('Original')
ax[0].axis('off')

#Plotting the histogram and the two threshold obtained from mutli-Otsu
ax[1].hist(image.ravel(), bins=255)
ax[1].set_title("Histogram")
for thresh in thresholds:
    ax[1].axvline(thresh, color='r')
    
    
#Plotting the Multi Otsu result
ax[2].imshow(regions, cmap='Accent')
ax[2].set_title('Multi-Otsu result')
ax[2].axis('off')

plt.subplots_adjust() 

plt.show()

   
    
    
    
    
    
