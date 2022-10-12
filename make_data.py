from turtle import circle
import numpy as np
import cv2
import math


image_width = 500
image_height = 500


image = np.zeros((image_width, image_height, 3), np.uint8)

window_name = "Image"

center_coordinates = (100, 50)

axesLength = (100, 50)

angle = 0

startAngle = 0

endAngle = 360

# Blue color in BGR
# color = (255, 0, 0)
color = (255, 255, 255)

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
for x in range(100, image_width - 100, 100):
    for y in range(100, image_height - 100, 100):
        ellip_pos.append((x, y))
        # cv2.imshow(window_name, image)
        # cv2.waitKey()
        # image = np.zeros((500, 500, 3), np.uint8)

# circle_pos = []
# for x in range(50,450):
#     for y in range(50,450):
#         circle_pos.append((x,y))

degree = []
for deg in range(0, 359, 10):
    degree.append(deg)

# math.tan(a)

# cv2.imwrite("temp.jpg", image)

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
contours, _ = cv2.findContours(img_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# print(contours)

count = 0

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
            x, y, w, h = rect
            ellip_bbox.append((e_pos[0], e_pos[1], w / 2, h / 2))
            obs_box_pos_list = []
            for x in range(int(e_pos[0] - w / 2), int(e_pos[0] + w / 2), 50):
                for y in range(int(e_pos[1] - h / 2), int(e_pos[1] + h / 2), 50):
                    obs_box_pos_list.append((x, y))

            for index in range(len(obs_box_pos_list)):
                image_end = np.copy(image)
                image_end = cv2.rectangle(
                    image_end,
                    (
                        int(
                            obs_box_pos_list[len(obs_box_pos_list) - 1 - index][0] - 40
                        ),
                        int(
                            obs_box_pos_list[len(obs_box_pos_list) - 1 - index][1] - 40
                        ),
                    ),
                    (
                        int(
                            obs_box_pos_list[len(obs_box_pos_list) - 1 - index][0] + 40
                        ),
                        int(
                            obs_box_pos_list[len(obs_box_pos_list) - 1 - index][1] + 40
                        ),
                    ),
                    color,
                    thickness=-1,
                )

                image_end = cv2.circle(
                    image_end,
                    (obs_box_pos_list[index][0], obs_box_pos_list[index][1]),
                    40,
                    color,
                    thickness=-1,
                )

                # print(e_pos[0], e_pos[1], w / 2, h / 2)
                cv2.imshow(window_name, image_end)
                cv2.waitKey()

                count += 1
                # cv2.imwrite(str(count) + ".jpg", image_end)
                # if count == 2:
                #     break

# print(count)
