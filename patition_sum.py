def recursiveSol(arr, _sum, currIndex):
    # base condition
    if _sum == 0:
        return True

    if currIndex >= len(arr) or _sum < 0:
        return False

    if arr[currIndex] <= _sum:
        choice1 = recursiveSol(arr, _sum - arr[currIndex], currIndex + 1)

        choice2 = recursiveSol(arr, _sum, currIndex + 1)

        return choice1 or choice2

    choice = recursiveSol(arr, _sum, currIndex + 1)

    return choice
  
def recursiveSolMemo(dp, arr, _sum, currIndex):
    # base condition
    if _sum == 0:
        return True

    if currIndex >= len(arr) or _sum < 0:
        return False

    if dp[currIndex][_sum] == -1:
        if arr[currIndex] <= _sum:
            choice1 = recursiveSolMemo(dp, arr, _sum - arr[currIndex], currIndex + 1)

            choice2 = recursiveSolMemo(dp, arr, _sum, currIndex + 1)

            dp[currIndex][_sum] = choice1 or choice2

            return dp[currIndex][_sum]

        dp[currIndex][_sum] = recursiveSolMemo(dp, arr, _sum, currIndex + 1)

        return dp[currIndex][_sum]

    return dp[currIndex][_sum]
#########################################
    s = sum(nums)

    if s % 2 != 0:
      return False

    dp = [[-1 for i in range(int(s / 2) + 1)] for y in range(len(nums))]

    return recursiveSolMemo(dp, nums, int(s / 2), 0)
