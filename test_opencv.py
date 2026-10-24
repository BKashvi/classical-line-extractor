import cv2
import numpy as np
print("open cv is working")
print("version: ", cv2.__version__)

import os

image_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "images","road.jpg")
print("Image path: ", image_path)
image=cv2.imread(image_path)


if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    print("Image shape: ", image.shape)

#HSV COLOUR SPACE
hsv_image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#FILTER WHITE AND YELLOW LINES
hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

white_lower=np.array([0,0,180])
white_upper=np.array([180,60,255])
white_mask=cv2.inRange(hsv, white_lower, white_upper)

yellow_lower=np.array([15,70,80])
yellow_upper=np.array([40,255,255])
yellow_mask=cv2.inRange(hsv, yellow_lower, yellow_upper)

lane_mask=cv2.bitwise_or(white_mask, yellow_mask)
cv2.imshow("white Lane Mask", white_mask)
cv2.imshow("yellow Lane Mask", yellow_mask)
cv2.imshow("Lane Mask", lane_mask)


#GAUSSIAN BLUR AND CANNY EDGE DETECTION
lane_mark=cv2.bitwise_or(white_mask, yellow_mask)
blurred_lane_mark=cv2.GaussianBlur(lane_mark, (5,5), 0)
edges=cv2.Canny(blurred_lane_mark, 50, 150)
cv2.imshow("Canny Edges", edges)
cv2.imshow("Blurred Lane Mark", blurred_lane_mark)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#ROI MASKING
height, width=edges.shape
mask=np.zeros_like(edges)
polygon=np.array([[
    (int(width*0.05), height-1),
    (int(width*0.40), int(height*0.55)),
    (int(width*0.60), int(height*0.55)),
    (int(width*0.95), height-1)
]], dtype=np.int32)

cv2.fillPoly(mask, polygon, 255)
masked_edges=cv2.bitwise_and(edges, mask)
cv2.imshow("Masked Edges", masked_edges)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


