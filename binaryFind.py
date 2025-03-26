
def binaryFind(number, array):
  halfArray=[]
  halfIndex=len(array)//2
  halfElement=array[halfIndex]
  if number==halfElement: return halfElement
  else:
      if number>halfElement:
        halfArray=array[halfIndex+1:]
      if halfElement>number:
        halfArray=array[:halfIndex]
  return binaryFind(number, halfArray)



