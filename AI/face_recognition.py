import imp
import cv2
import dlib

#read the image 
img = cv2.imread("D:\code\codePython\AI\pic_test.jpg")

#convert img to grayscale: 3D -> 2D(anh den trang)
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

#dlib: load Face Recognition Detector
face_detector = dlib.get_frontal_face_detector()

#use detector to find face landmarks
faces = face_detector(gray)

for face in faces:
    x1 = face.left() #left point
    y1 = face.top() #top point
    x2 = face.right() #right point
    y2 = face.bottom() #bottom point
    #draw a rectangle
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=3)

#show the image
cv2.imshow(winname="Face Recongnition App", mat=img)


#wait for a key press to exit
cv2.waitKey(delay=0)

#close all windows
cv2.destroyAllWindows()