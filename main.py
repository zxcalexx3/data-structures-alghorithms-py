from binaryFind import binaryFind
import random
import time

def testBinaryFind():
  startSeconds=time.time()
  for i in range(100):
    array=[]
    for i in range(1000):
      element=random.randint(1,1000)
      array.append(element)
    numberIndex=random.randint(0,999)
    number=array[numberIndex]
    array.sort()
    print(binaryFind(number,array), number)
  seconds1=time.time()
  return(seconds1-startSeconds)
    
print(testBinaryFind()) 