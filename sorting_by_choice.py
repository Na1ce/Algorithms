our_array = [2, 6, 3, 8, 4, 1]


def find_min(arr):
    smallest_num = arr[0]
    smallest_idx = 0
    for el in range(1, len(arr)):
        if arr[el] < smallest_num:
            smallest_num = arr[el]
            smallest_idx = el
    return smallest_idx


def sorting_by_choice(arr):
    newArr = []
    for el in range(len(arr)):
        smaller = find_min(arr)
        newArr.append(arr.pop(smaller))
    return newArr


print(sorting_by_choice(our_array))
