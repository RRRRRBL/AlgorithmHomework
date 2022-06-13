def fibonacci(num, counter):     # dynamic
    dp = [0 for i in range(num+1)]
    for i in range(num+1):
        if i == 1 or i ==2:
            dp[i] = 1
        else:
            dp[i] = dp[i-1] + dp[i-2]
            counter[0] += 1

    return dp


def dac_fibonacci(num, counter):
    dp = [0 for i in range(num+1)] # divide and conquer
    dac(num, dp, counter)
    print(num)
    return dp


def dac(number, dp, counter):
    if number == 1 or number == 2:
        dp[number] = 1
    else:
        dac(number - 2, dp, counter)
        dac(number - 1, dp, counter)
        dp[number] = dp[number-1] + dp[number-2]
        counter[0] += 1


num_ = 10
fib_counter = [0]
dac_counter = [0]
dp_array = dac_fibonacci(num_, dac_counter)
dp_array2 = fibonacci(num_, fib_counter)
print("DP 结果：", end="")
print(dp_array)
print("DAC 结果：", end="")
print(dp_array2)
print("DP 加操作此次数：", end="")
print(fib_counter)
print("DAC 加操作此次数：", end="")
print(dac_counter)