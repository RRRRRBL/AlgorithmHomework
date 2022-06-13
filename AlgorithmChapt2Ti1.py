import random
import time


def calculate_reminder(num):  # 完成求余计算
    return (7 * num + 5) % 521


def same_linear_remainder(num_numbers):
    number_list = [random.randint(1, 100)]  # 存放随机数的列表,给定一个初始值，便于生产随机数
    for i in range(num_numbers - 1):
        number_list.append(calculate_reminder(number_list[i]))
    number_list[0] = calculate_reminder(number_list[num_numbers - 1])  # 对第一个数随机化
    return number_list


def knapasckdp(weight, value, space):
    dp = []
    dp = [[0 for i in range(space + 1)] for j in range(len(weight) + 1)]
    for i in range(1, len(weight) + 1):
        for j in range(1, space + 1):
            dp[i][j] = dp[i - 1][j]
            if weight[i - 1] <= j:
                if dp[i][j] < dp[i - 1][j - weight[i - 1]] + value[i - 1]:
                    dp[i][j] = dp[i - 1][j - weight[i - 1]] + value[i - 1]
    return dp


start = time.time()
n = 10
weights = same_linear_remainder(n)
print(weights)
values = same_linear_remainder(n)
spaces = 2000
result = knapasckdp(weights, values, spaces)
for i in range(n):
    print(result[i])
end = time.time()
print("程序运行时间：", end = "")
print(end - start)
