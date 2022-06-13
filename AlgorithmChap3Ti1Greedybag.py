import random
import time


def calculate_reminder(num):  # 完成求余计算
    return (7 * num + 5) % 521


def same_linear_remainder(num_numbers):
    number_list = [random.randint(1, 100)]  # 存放随机数的列表,给定一个初始值，便于生产随机数
    for i in range(num_numbers - 1):
        number_list.append(calculate_reminder(number_list[i])+1)
    number_list[0] = calculate_reminder(number_list[num_numbers - 1])  # 对第一个数随机化
    return number_list


class Products:  # 存放每一个物品的信息，价值，重量，序号等。
    weight = 0
    value = 0
    vw = 0
    order = 0  # 记录当前物品的序号

    def __init__(self, weight, value, i):
        self.weight = weight
        self.value = value
        self.order = i
        self.vw = value / weight


def knapsack_greedy(pro_list, num, space):
    result = [0 for j in range(num)]
    spare_space = space
    s = 0
    for s in range(num):
        if pro_list[s].weight > spare_space:
            break
        result[products_list[s].order] = 1
        spare_space -= pro_list[s].weight
    if s <= (num - 1):  # 解决如果是break的情况下，该物品装不完全的情况
        result[s] = spare_space / pro_list[s].weight
    print(result)   # 打印结果


def find_vw(products):  # 对象列表排序
    return products.vw


number = 2000
space = 100
products_list = []
weights = same_linear_remainder(number)
values = same_linear_remainder(number)
for i in range(number):
    products_list.append(Products(weights[i], values[i], i))
products_list.sort(reverse=True, key=find_vw)  # 根据V/W进行排序
start = time.time()
knapsack_greedy(products_list, number, space)
end = time.time()
print("程序运行时间：", end = "")
print(end - start)

