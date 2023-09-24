def bubble_sort(number):
    n = len(number)
    for i in range(n):
        for j in range(0, n - i - 1):
            if number[j] > number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]
    return number


if __name__ == "__main__":
    number = [9, 22, 16, 8, 14, 10, 25, 26]
    bubble_sort(number)
    print("Отсортированный список", number)


def bubble_sort(val, a):
    resultOk = False
    first = 0
    last = len(a) - 1
    pos = -1
    while first < last:
        mid = (first + last) // 2
        if val == a[mid]:
            first = mid
            last = mid
            resultOk = True
            pos = mid
        elif val > a[mid]:
            first = mid + 1
        else:
            last = mid - 1

    if (val == a[first]):
        resultOk = True
        pos = first
    if (resultOk):
        print("Элемент найден")
        print(pos)
    else:
        print("Элемент не найден")


bubble_sort(9, [1, 2, 3, 4, 5, 6, 7, 8, 9])
