list_to_10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Enter your nubmer:')
search_num = int(input())


def binary_search(our_list, num):
    low = 0
    high = len(our_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if num == mid:
            return print('We know your namber!')
        if num < mid:
            high = mid - 1
            print('One more time...')
        else:
            low = mid + 1
            print("One more time...")
    return print('The number does not exist in the list')


binary_search(list_to_10, search_num)

