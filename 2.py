import cv2

x=input ("введите название изображения")
image = cv2.imread("Images/"+x+".jpg")
cv2.imshow("Slicend image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
