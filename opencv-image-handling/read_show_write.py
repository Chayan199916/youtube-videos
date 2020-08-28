#importing module
import cv2 # pip install opencv-python

# what is image? 

# #reading image
# img = cv2.imread('image1.jpg', 0) # IMREAD_COLOR = 1, IMREAD_GRAYSCALE = 0
# Y' = 0.299R' + 0.587G' + 0.114B'
# print(img)
# #showing image
# cv2.namedWindow('my_window', cv2.WINDOW_NORMAL) #resizing window with this flag
# cv2.imshow("my_window", img) #window name, image object
# cv2.waitKey(0) #keyboard binding; takes time in ms to wait for a kb event; if 0 is passed waits indefinitely
# cv2.destroyAllWindows() #destroying windows;for specific use windowname and destroyWindow()

# #writing image
# cv2.imwrite('saved_gray_image.png', img)

# resizing image
# resized_image = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))
# cv2.imshow("my_window", resized_image) #window name, image object
# cv2.waitKey(0) #keyboard binding; takes time in ms to wait for a kb event; if 0 is passed waits indefinitely
# cv2.destroyAllWindows()

# print(img.shape) # tuple
# cv2.imwrite('saved_resized_gray_image.png', resized_image)

# performing operation based on keyboard i/p

img = cv2.imread('image1.jpg', 0)

cv2.namedWindow('my_window', cv2.WINDOW_NORMAL)
cv2.imshow('my_window', img)

key = cv2.waitKey(0)

if key == 13: #enter key
    cv2.destroyAllWindows()
elif key == ord('s'): #ord returns unicode of 1 length string; chr works in opposite way
    cv2.imwrite('saved_gray_image.png', img)
    cv2.destroyAllWindows()

# chr(65) = "A"
# ord("A") = 65

