def test_func():
    for i in range(10):
        yield i


for i in range(10):
    print(next(test_func()))
    print(next(test_func()))


def bubble_sort(num):
    for i in range(len(num)):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num


def merge_sort(num):
    if len(num) <= 1:
        return num
    mid = len(num) // 2
    left = merge_sort(num[:mid])
    right = merge_sort(num[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result
