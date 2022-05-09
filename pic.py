# -*- coding: utf-8 -*-

import cv2

xmin1 = 210
#xmin1 = 90
xmax1 = xmin1+20
ymin1 = 10
#ymin1 = 90
ymax1 = ymin1+20

xmin2 = 150
#xmin2 = 175
xmax2 = xmin2+20
ymin2 = 40
#ymin2 = 80
ymax2 = ymin2+20

file = 'img_64152_val_13_pred_n2c.png'

image = cv2.imread(file)
cv2.rectangle(image, (xmin1, ymin1), (xmax1, ymax1), (255, 0, 0), 2)
cv2.rectangle(image, (xmin2, ymin2), (xmax2, ymax2), (0, 0, 255), 2)
cv2.imwrite('whole_'+file, image)

image1 = image[ymin1:ymax1, xmin1:xmax1]
cv2.rectangle(image1, (0, 0), (18, 18), (255, 0, 0), 1)
cv2.imwrite('rect1_'+file, image1)

image2 = image[ymin2:ymax2, xmin2:xmax2]
cv2.rectangle(image2, (0, 0), (18, 18), (0, 0, 255), 1)
cv2.imwrite('rect2_'+file, image2)