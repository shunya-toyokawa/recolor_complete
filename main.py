import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageOps
from copy import deepcopy
import  time



person = np.array(Image.open("person.jpg"))
origin = Image.fromarray(deepcopy(person))


mask = np.array(Image.open("mask.png"))

canvas = np.zeros_like(mask)


pallet= [255,85,0]

for e in range(mask.shape[0]):
    for i in range(mask.shape[1]):


        if (mask[e][i][0] == pallet[0]) & (mask[e][i][1] == pallet[1]) & (mask[e][i][2] == pallet[2])==False:

            person[e][i] =[255,255,255]
            

            if (e%100==0) &(i%1000==0):
                print(e,"/1000")
        else:
            canvas[e][i]=[255,255,255]
            #print(canvas[e][i])




garment  =Image.fromarray(person)
#out.save("cutout_garment.png")
garment_mask = Image.fromarray(canvas).convert("L")
#canvas.save("cutout_garment_mask.png")






gray = ImageOps.grayscale(garment)
#print(gray.mode)
out =ImageOps.colorize(gray, black=(0, 70, 20), white=(255, 255, 255))
out.putalpha(garment_mask)
out.save("out_finaly.png")


garment_mask_reverse=cv2.bitwise_not(canvas)
garment_mask_reverse= Image.fromarray(garment_mask_reverse).convert("L")
#garment_mask_reverse.save("re.png")
origin.putalpha(garment_mask_reverse)
origin.save("reout.png")


#add
out = cv2.imread("out_finaly.png",cv2.IMREAD_UNCHANGED)
origin = cv2.imread("reout.png")
x1, y1, x2, y2 = 0, 0, out.shape[1], out.shape[0]
origin[y1:y2, x1:x2] = origin[y1:y2, x1:x2] * (1 - out[:, :, 3:] / 255) + out[:, :, :3] * (out[:, :, 3:] / 255)
origin = cv2.cvtColor(origin, cv2.COLOR_BGR2RGB)
origin = Image.fromarray(origin)
origin.save("result.png",)

