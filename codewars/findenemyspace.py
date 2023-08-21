def ArrayChallenge(arr):
  
  playerPos = None
  for i in range(len(arr)):
    if arr[i] == 1:
      playerPos = i

  def findEnemyRight(lst, idx):
    count = 0
    for i in range(idx, len(lst)):
      if lst[i] == 2:
        return count
      else:
        count += 1

  def findEnemyLeft(lst, idx):
    count = 0
    for i in range(idx, 0, -1):
      if lst[i] == 2:
        return count
      else:
        count += 1     
  
  enemyRight = findEnemyRight(arr,playerPos)
  enemyLeft = findEnemyLeft(arr,playerPos)

  if enemyLeft == None and enemyRight == None:
    return 0
  elif enemyLeft == None:
    return enemyRight
  else:
    return enemyLeft


print(ArrayChallenge(input()))