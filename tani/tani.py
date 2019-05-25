import tensorflow as tf
from data import MNISTDataHandler
import numpy as np
import PIL.Image as pil
from tensorflow.examples.tutorials.mnist import input_data


 

def takeSampleData(sample, nr_of_images):
  
  batch_x, batch_y = dh.sample_pair(nr_of_images,sample)
  #print(len(batch_x ), len(batch_x[0]), len(batch_x[0][0]), batch_x[0][0][0] )
  #print()
  #print()
  #print(len(batch_y ), len(batch_y[0]))
  
  
  #img = pil.fromarray(np.uint8(testImage * 255) , 'L')
  #img.show()

  #testImage = (np.array(batch_y[0], dtype='float')).reshape(28,28)
  #img = pil.fromarray(np.uint8(testImage * 255) , 'L')
  #img.show()

  for i in range(nr_of_images):
    testImage = (np.array(batch_x[i], dtype='float')).reshape(28,28)
    img = pil.fromarray(np.uint8(testImage * 255) , 'L')
    img.show()



  testImage = (np.array(batch_x[0], dtype='float')).reshape(28,28)
  return testImage

def main():
  for i in range(4):
    testImage = takeSampleData(i,1)
  img = pil.fromarray(np.uint8(testImage * 255) , 'L')
  img.show()

  

  

if __name__ == "__main__":
  dh = MNISTDataHandler("MNIST_data", is_train=True)
  main()

# TODO
