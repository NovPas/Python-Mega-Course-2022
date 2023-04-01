import cv2

img=cv2.imread('galaxy.jpg', cv2.IMREAD_GRAYSCALE)

print(type(img))
print(img)
print(img.shape)
print(img.size)
print(img.ndim)

resizedValue=4
resized_image=cv2.resize(img,(int(img.shape[1]/resizedValue),int(img.shape[0]/resizedValue)))
cv2.imwrite('resized_image.jpg',resized_image)

cv2.imshow('Galaxy', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()