import cv2

face_cascade = cv2.CascadeClassifier("/Users/sayannath/Desktop/haarcascade_frontalface_default.xml")

img1 = cv2.imread("/Users/sayannath/Desktop/Apps/BITMOJI/6.png", 1)

# The 3d Matrix
print(img1)

# The Type of matrix 3d
print(type(img1))

# Shape of a RGB image
print(img1.shape)  # It returns the number of columns rows and the dimension of the Matrix

img2 = cv2.imread("/Users/sayannath/Downloads/2.jpg", 0)

# The 2d Matrix
print(img2)

# The Type of matrix 2d
print(type(img2))

# Shape of a RGB image
print(img2.shape)  # It returns the number of columns rows and the dimension of the Matrix

gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5)

for x,y,w,h in faces:
    img1 = cv2.rectangle(img1, (x,y), (x+w,y+h), (0,255,0), 3)


cv2.imshow("Sayan", img1)
cv2.waitKey(100000)
cv2.destroyAllWindows()

