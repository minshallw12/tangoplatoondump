import itertools

def ArrayChallenge(arr):

  my_max = max(arr)

  new_lst = []
  for num in arr:
    if num != my_max:
      new_lst.append(num)

  my_combos = []

  for l in range(len(new_lst)+1):
    for subset in itertools.combinations(new_lst, l):
      my_combos.append(subset)
   
  for subset in my_combos:
    if sum(subset) == my_max:
      return 'true'

  return 'false'  