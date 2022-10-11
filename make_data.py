from turtle import circle
import numpy as np
import cv2
import math 

image = np.zeros((500, 500, 3), np.uint8)

window_name = "Image"

center_coordinates = (100, 50)

axesLength = (100, 50)

angle = 0

startAngle = 0

endAngle = 360

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of -1 px
thickness = -1

# Using cv2.ellipse() method
# Draw a ellipse with blue line borders of thickness of -1 px


# image = cv2.ellipse(
    # image, center_coordinates, axesLength, angle, startAngle, endAngle, color, thickness
    # image, (0, 0), axesLength, angle, startAngle, endAngle, color, thickness
# )


# image, center_coordinates, radius, color, thickness
# image = cv2.circle(image, (0, 0), 50, (0, 255, 0), thickness)




ellip_pos = []
for x in range(100,400):
    for y in range(100,400):
        ellip_pos.append((x,y))
        # cv2.imshow(window_name, image)
        # cv2.waitKey()
        # image = np.zeros((500, 500, 3), np.uint8)

# circle_pos = []
# for x in range(50,450):
#     for y in range(50,450):
#         circle_pos.append((x,y))

degree = []
for deg in range(359):
    degree.append(deg)

# math.tan(a)

# cv2.imwrite("temp.jpg", image)

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
contours, _ = cv2.findContours(img_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# print(contours)

ellip_bbox = []
for e_pos in ellip_pos:
    for angle in degree:
        image = np.zeros((500, 500, 3), np.uint8)
        image = cv2.ellipse(
                image, e_pos, axesLength, angle, startAngle, endAngle, color, thickness
            )
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(img_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            rect = cv2.boundingRect(c)
            x,y,w,h = rect
            ellip_bbox.append((e_pos[0],e_pos[1], w/2, h/2))
            # image = cv2.rectangle(
            #     image, 
            #     (int(e_pos[0]-w/2), int(e_pos[1]-h/2)), 
            #     (int(e_pos[0]+w/2), int(e_pos[1]+h/2)), 
            #     color, thickness = 2)
            # print(e_pos[0],e_pos[1],w/2,h/2)
            obs_box_pos = []
            for x in range(int(e_pos[0]-w/2), int(e_pos[0]+w/2),10):
                for y in range(int(e_pos[1]-h/2), int(e_pos[1]+h/2),10):
                    image = np.zeros((500, 500, 3), np.uint8)
                    image = cv2.ellipse(
                        image, e_pos, axesLength, angle, startAngle, endAngle, color, thickness
                        )
                    image = cv2.rectangle(
                        image, 
                        (int(x - 20), int(y - 20)), 
                        (int(x + 20), int(y + 20)), 
                        color, thickness = 2)
                    cv2.imshow(window_name, image)
                    cv2.waitKey()
                    
        
        # cv2.imshow(window_name, image)
        # cv2.waitKey()



