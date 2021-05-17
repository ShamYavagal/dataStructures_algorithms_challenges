arr = [1, 2, 3, 4, 3, 2, 1, 2, 5]

def find_max_sliding_window(arr, window_size):
    result = []
    index = 0
    while window_size <= len(arr):
        value = sorted(arr[index:window_size])
        result.append(value[-1])
        window_size += 1
        index += 1
    return result

find_max_sliding_window(arr, 4)