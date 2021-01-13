# Directories
import cv2
import os

#To create the folder for saving the dataset
os.mkdir('Data_set')

#To threshold the hand 
def thresh_file(img):   
    h,w = img.shape[:2]
    img = cv2.GaussianBlur(img, (9, 9), 0)
    bw_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    for i in range(h):
        for j in range(w):
            if bw_image[i][j] > 11:
               bw_image[i][j] = 255
            else:
               bw_image[i][j] = 0

    return bw_image

# to put the binary image in folder Data_set 
for folder in os.listdir('asl'):

    os.mkdir(os.path.join('Data_set',folder))

    for filename in os.listdir(os.path.join('asl',folder)):
        img = cv2.imread(os.path.join('asl',folder, filename))
        bw_img = thresh_file(img)
        cv2.imwrite(os.path.join('Data_set', folder, filename), bw_img)
    print("Folder", folder, "Transfered")
 


































