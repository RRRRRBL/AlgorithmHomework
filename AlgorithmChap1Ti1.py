import random
import math


def calculate_reminder(num):  # 完成求余计算
    return (7 * num + 5) % 521


def same_linear_remainder(num_numbers):
    number_list = [random.randint(1, 100)]  # 存放随机数的列表,给定一个初始值，便于生产随机数
    for i in range(num_numbers - 1):
        number_list.append(calculate_reminder(number_list[i]))
    number_list[0] = calculate_reminder(number_list[num_numbers - 1])  # 对第一个数随机化
    return number_list


def swap(list_, index1, index2):
    temp = list_[index1]
    list_[index1] = list_[index2]
    list_[index2] = temp


def bubble_sort(list1, num1, counts):  # 冒泡排序-升序
    to_sort_length = num1
    while True:
        if to_sort_length == 1:  # 判断剩余待排序列表长度
            break
        for i in range(to_sort_length - 1):
            counts[0] = counts[0] + 1
            if list1[i] > list1[i + 1]:
                swap(list1, i, i + 1)
        to_sort_length = to_sort_length - 1


def merger_list(to_merge_list, start1, end1, start2, end2, counts,):  # 合并排序—升序
    temp_list = []  # 暂存元素列表
    start_mark = start1  # 记录起始位置
    while start1 <= end1 and start2 <= end2:
        counts[0] = counts[0] + 1
        if to_merge_list[start1] < to_merge_list[start2]:
            temp_list.append(to_merge_list[start1])
            start1 = start1 + 1
        else:
            temp_list.append(to_merge_list[start2])
            start2 = start2 + 1

    counts[0] = counts[0] + 1
    if start1 > end1:  # 如果是列表一已经全都放入了暂存列表，则将列表二中元素依次放入
        while start2 <= end2:
            counts[0] = counts[0] + 1
            temp_list.append(to_merge_list[start2])
            start2 = start2 + 1
    else:
        while start1 <= end1:
            counts[0] = counts[0] + 1
            temp_list.append(to_merge_list[start1])
            start1 = start1 + 1
    for i in range(len(temp_list)):
        to_merge_list[start_mark + i] = temp_list[i]


def merge_sort(list2, start, end, counts, size_counter):  # 合并排序—升序
    size_counter.append(abs(start-end))
    counts[0] = counts[0] + 1
    if start >= end:
        return
    middle = int((start + end) / 2)
    merge_sort(list2, start, middle, counts, size_counter)
    merge_sort(list2, middle + 1, end, counts, size_counter)
    merger_list(list2, start, middle, middle + 1, end, counts)


def quick_sort(list3, first, last, counts, size_counter):  # 快速排序-升序
    size_counter.append(abs(first-last))
    counts[0] = counts[0] + 1
    if first >= last:
        return
    markable_number = list3[first]
    head = first + 1
    rear = last
    while head != rear:  # 快排核心过程
        counts[0] = counts[0] + 1
        if list3[head] <= markable_number and head < rear:
            head = head + 1
        counts[0] = counts[0] + 1
        if list3[rear] >= markable_number and rear > head:
            rear = rear - 1
        swap(list3, head, rear)
    counts[0] = counts[0] + 1
    if list3[head] < markable_number:  # 判断被用作pivot的数需不需要换位置
        swap(list3, head, first)
    counts[0] = counts[0] + 1
    if first == last - 1:  # 此时只有两个元素，且已经有序，不用再调用递归
        return
    quick_sort(list3, first, head - 1, counts, size_counter)  # 进行递归
    quick_sort(list3, head, last, counts, size_counter)


counts_merge = [0]
counts_quick = [0]
counts_bubble = [0]
size_counter_merge = []
size_counter_quick = []

num_needed = int(input("请输入您需要的随机数个数\n"))
random_num_list = same_linear_remainder(num_needed)  # 调用函数获取列表
print("初始列表", end="")
print(random_num_list)
bubble_sort_list = random_num_list.copy()
merger_sort_list = random_num_list.copy()
quick_sort_list = random_num_list.copy()

bubble_sort(bubble_sort_list, num_needed, counts_bubble)
print("冒泡排序结果", end='')
print(bubble_sort_list)
print("冒泡排序比较次数：", end='')
print(counts_bubble[0])

merge_sort(merger_sort_list, 0, num_needed - 1, counts_merge, size_counter_merge)
print("合并排序结果", end='')
print(merger_sort_list)
print("合并排序比较次数：", end='')
print(counts_merge[0])
print("合并排序子问题规模", end='')
print(size_counter_merge)


quick_sort(quick_sort_list, 0, num_needed - 1, counts_quick, size_counter_quick)
print("快速排序结果", end='')
print(quick_sort_list)
print("快速排序比较次数：", end='')
print(counts_quick[0])
print("快速排序子问题规模", end='')
print(size_counter_quick)