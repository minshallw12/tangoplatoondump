def ArrayChallenge(arr):

  def findRange(num1, num2):
    my_range=[]
    for num in range(num1, num2+1):
      my_range.append(num)
    return my_range
  
  range1 = findRange(arr[0], arr[1])
  range2 = findRange(arr[2], arr[3])

  def countOverlap(arr1, arr2):
    count=0
    for i in range(len(arr1)):
      if arr1[i] in arr2:
        count=count+1
    return count

  overlap = countOverlap(range1,range2)

  if overlap >= arr[4]:
    return 'true'
  return 'false'

# keep this function call here 
print(ArrayChallenge(input()))