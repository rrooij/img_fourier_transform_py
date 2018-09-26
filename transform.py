#!/usr/bin/env python3

import cv2
import numpy as np
import sys
from time import sleep

def show_img(img):
    cv2.imshow('image', img_back)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread(sys.argv[1],0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
f_ishift = np.fft.ifftshift(fshift)
d_shift = np.array(np.dstack([f_ishift.real,f_ishift.imag]))
img_back = cv2.idft(d_shift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
show_img(img_back)
