#importing required libraries
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
import os
#import matplotlib.pyplot as plt
from skimage.color import rgb2gray
#reading the image
def hogFeatures(imgPath='NA',category="NA"):
	UPLOAD_DIR=os.getcwd()+"\\DataSet\\"
	UPLOAD_DIR1=os.getcwd()+"\\DataSet\\train\\"
	UPLOAD_DIR2=os.getcwd()+"\\DataSet\\test\\"
	print("type="+category)
	imgpath=UPLOAD_DIR1+category+"\\"+imgPath
	print(imgpath)
	original = imread(imgpath)
	img = rgb2gray(original)
	#plt.axis("off")
	#plt.imshow(img)
	#print(img.shape)

	#resizing image
	#resized_imgg = resize(img, (128*4, 64*4))
	#resized_img = rgb2gray(resized_imgg)
	resized_img = rgb2gray(img)
	#plt.axis("off")
	#plt.imshow(resized_img)
	#plt.show()
	print(resized_img.shape)

	#creating hog features
	fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8),
						cells_per_block=(2, 2), visualize=True)
	return hog_image
	#print(hog_image)
	#print(fd.shape)
	#print(hog_image.shape)
	#plt.axis("off")
	#plt.imshow(hog_image, cmap="gray")
	#plt.show()

	# save the images
	#plt.imsave("E:\\python\\resized_img.jpg", resized_img)
	#plt.imsave("E:\\python\\hog_image.jpg", hog_image, cmap="gray")