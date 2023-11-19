import numpy
import cv2 

cap = cv2.VideoCapture("D:/FAST_NUCES/7thSemester/DLP/Assignment/Assignment3/Datasets/DatasetQ1/traffic_Islamabad_Police.mp4")
ret, img = cap.read()

rows, cols, _ = img.shape

while True:
    ret, img = cap.read()

    img = img[0: rows, 0: cols]


    #Show Image
    cv2.imshow("Img", img)
    key = cv2.waitKey(33)
    if key == 27:
        break

cv2.destroyAllWindows()
