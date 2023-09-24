def bubble_sort(number):
    n = len(number)
    for i in range(n):
        for j in range(0, n - i - 1):
            if number[j] > number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]


if __name__ == "__main__":
    number = [9, 22, 16, 8, 14, 10, 25, 26]
    bubble_sort(number)
    print("Отсортированный список", number)


def binary_search(search, number):
    low, high = 0, len(number) - 1
    while low <= high:
        mid = (low + high) // 2
        if number[mid] == search:
            return mid
        elif number[mid] < search:
            low = mid + 1
        else:
            high = mid - 1

    if low <= high:
        return 'Element searched'
    else:
        return 'Element not searched'


print(binary_search(5, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
