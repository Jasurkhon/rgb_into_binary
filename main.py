#importing opencv library
import cv2

# path where image is stored just copy and paste full path between quotes
path ='photo.jpg'

#in order to read image use imread function which takes 2 arguments: path where image is in and flag with value 0 which means that image will be read in grayscale mode
gray_img = cv2.imread(path,0)
#displaying image in grayscale mode. This function takes 2 arguments: string "Grayscalse Img" which will be assigned to the window and image to be displayed
cv2.imshow('Grayscale Img', gray_img)
# waits for a key event occuring
cv2.waitKey(0)
#to convert image to binary use threshold function. It takes 4 arguments: grayscale image for which we want to apply thresholding operation, value of threshold with range between 0 and 255, user's value for which a pixel must be converted, and finally thresholding type in our case THRESH_BINARY 
thresh, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
#displaying image in binary mode. This function takes 2 arguments: string "Binary Img" which will be assigned to the window and image to be displayed
cv2.imshow('Binary Img', binary_img)
# waits for a key event occuring
cv2.waitKey(0)
# Window shown waits for any key pressing event to destroy the previously created windows
cv2.destroyAllWindows()



