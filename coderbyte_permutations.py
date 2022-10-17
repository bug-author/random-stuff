def MathChallenge(num):

  # code goes here
  # we need to find permutations of this number
  num = str(num)
  # recursion could be used
  #

  # 98 -> 98, 89
  # 598 -> 3! 589, 598, 958, 985, 859, 895 
  def recursiveSol(processed, unprocessed):
    # base condition
    if len(unprocessed) <= 0:
      permuts.append(processed)
      return
    
    # find permutations
    for i in range(0, len(unprocessed)):
      recursiveSol(processed+unprocessed[i], unprocessed[:i] + unprocessed[i+1:])

  permuts = []
  
  p = ""
  up = str(num)
  recursiveSol(p, up)

  permuts = [int(p) for p in permuts]

  # now check if any permutation is prime, if yes return 1
  # prime numbers are divisible by 1 and themselves only
  for permut in permuts:
    # if number is 0 or 1 -> not prime
    # if number is 2 -> prime
    # for other numbers if number is completely divisible by any number, it is not prime
    # completely divisible means % == 0
    flag = True
    if permut < 2:
      flag = False
    
    if permut == 2:
      return 1
    
    for x in range(3, permut):
      if permut % x == 0:
        # print(f'{permut}-{permut}%{x}')
        flag = False
    
    if flag:
      return 1
      


  return 0

# keep this function call here 
print(MathChallenge(input()))
