def binary_search(arr, target):
    (low, high) = 0, len(arr) - 1
    steps = 1

    while low <= high:
        stringify = list(range(low + 1, (high + 2)))
        print("Step", steps, ":", str(stringify))
        mid = (low + high) // 2
        steps += 1
        mid_arr = arr[mid]
        if mid_arr == target:
            return mid
        elif mid_arr < target:
            low = mid + 1
        elif mid_arr > target:
            high = mid - 1

    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
target = 2

result = binary_search(my_list, target)

if result != -1:
    print(f"{target} found at index {result}")

else:
    print("false number")