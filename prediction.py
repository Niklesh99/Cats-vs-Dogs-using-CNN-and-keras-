import cv2
import tensorflow as tf 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from tensorflow.keras.models import load_model

CATEGORIES=['Dooog','Cato']

image=r"C:\Users\Priya\Desktop\Projects-master\PY Ashish\Test_images\1 (2)"

def prepare(image):

	img_size=100
	img_array=cv2.imread(image,cv2.IMREAD_GRAYSCALE)
	new_array=cv2.resize(img_array,(img_size,img_size))
	return new_array.reshape(-1,img_size,img_size,1)

model = tf.keras.model.load_model(r"")
prediction=mdoel.predict([prepare(image)])
print(CATEGORIES[int(prediction[0][0])])

img=mpimg.imread(image)
imgplot=plt.imshow(img)
plt.title(CATEGORIES[int(prediction[0][0])])
plt.show()


