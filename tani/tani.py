import tensorflow as tf
from data import MNISTDataHandler
import numpy as np
import PIL.Image as pil
from tensorflow.examples.tutorials.mnist import input_data

import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import  graphviz_layout
import networkx as nx
import pandas as pd
import seaborn as sns

from modules.Components import Abstract, Context1, Context2, Actuator, Spektron
from modules.Veri import Veri
from modules.BaseStructure import BaseStructure
from pywt import wavedec
import random



def prepareImage(image):
  for i in range(28):
    for j in range(28):
      print(int(image[i][j]*256),end="\t")
    print()
  print()
  print()
  for i in range(28):
    for j in range(28):
      a=3
      if(image[i][j]==0 ):
        a=0
      elif(image[i][j] <=1/2):
        a=1
      elif(image[i][j] <= 3/4):
        a=2
      if(a==0):
        print (" ",end=" ")
      else:
        print(a,end=" ")
    print()
    
def takeSampleData(sample, nr_of_images, show =False):
  
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
  return batch_x[0]
  for i in range(nr_of_images):
    testImage = (np.array(batch_x[i], dtype='float')).reshape(28,28)
    if(show):
      img = pil.fromarray(np.uint8(testImage * 255) , 'L')
      img.show()

  testImage = (np.array(batch_x[0], dtype='float')).reshape(28,28)
  return testImage

def main():
  i=3
  #for i in range(4):
  testImage = takeSampleData(i,1)
  for i in range(28):
    print("\n",i,end="\t")
    for j in range(28):
      print(int(testImage[i][j]*256),end=" ")
  #prepareImage(testImage)
  #img = pil.fromarray(np.uint8(testImage * 255) , 'L')
  #img.show()

  v = Veri()

  ana = BaseStructure()

  #ana.addBranchEntropy([0,1,2,3,4])
  #ana.addBranchEntropy([0,1,2,3,4])
  #ana.addBranchEntropy([0,1,2,3,4])
  #ana.addBranchEntropy([0,1,2,3,4])
  #ana.addBranchEntropy([0,1,2,4,4])



  ana.agCizdir()


  return 0

  

  

if __name__ == "__main__":
  dh = MNISTDataHandler("MNIST_data", is_train=True)
  main()

# TODO
# 1. encode image forinput
# 2. build tree from input
# 3. display tree
# 4. clasify
# 5. deeper thinking
# 6. 