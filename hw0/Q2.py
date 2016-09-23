
# coding: utf-8

# In[15]:

from PIL import Image 
import numpy as np
import sys


# In[27]:

def rotate(image):
    lena = Image.open(image)
    lena_rotate = lena.rotate(180)
    lena_rotate.save("ans2.png")
    
if __name__=='__main__':
    #image = raw_input()
    rotate(sys.argv[1])
    

