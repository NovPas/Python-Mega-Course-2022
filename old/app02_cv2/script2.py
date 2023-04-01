import os
import cv2

source_folder = './sample_images/'
dest_folder = './resized_images/'

files = os.listdir(source_folder)

for filename in files:
    img=cv2.imread(source_folder+filename) 
    resized_image=cv2.resize(img,(100,100))
    cv2.imwrite(dest_folder+filename,resized_image)