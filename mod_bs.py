
def find_oldest_line(arr):
    """
    Find the oldest line
    """
    idx_s = 0
    idx_e = len(arr) - 1

    # This is not necessary, we will also detect this case in the while-loop
    if arr[idx_s] < arr[idx_e]:
        return idx_s

    while idx_s <= idx_e:
        idx_m = (idx_s + idx_e) // 2

        #-- Check whether idx_m is the turning point
        #-- Only check its prev/next number if this number at the end/start of the array
        # print(f'{idx_s} -- {idx_m} -- {idx_e}')
        # print(f'{arr[idx_s]} -- {arr[idx_m]} -- {arr[idx_e]}')
        if (idx_m == 0 or arr[idx_m] < arr[idx_m - 1]) \
                and (idx_m == len(arr) -1 or arr[idx_m] < arr[idx_m + 1]):
            return idx_m

        if arr[idx_s] > arr[idx_m]:
            idx_e = idx_m 
        elif arr[idx_m] > arr[idx_e]:
            idx_s = idx_m
        else:
            break

    # array is ascending totally
    return idx_s


def binary_search(arr, val):
    """Normal binary search """
    begin = 0
    end = len(arr) - 1

    while begin <= end:
        mid = (begin + end) // 2
        if arr[mid] < val:
            begin = mid + 1
        elif arr[mid] > val:
            end = mid - 1
        else:
            return mid

    return None


def find_val(arr, val):
    """Finish final question"""
    oldest_line = find_oldest_line(arr)
    if oldest_line == 0:
        return binary_search(arr, val)
    elif arr[0] <= val and val <= arr[oldest_line - 1]:
        return binary_search(arr[:oldest_line], val)
    elif arr[oldest_line] <= val and arr[-1] >= val:
        ret = binary_search(arr[oldest_line:], val)
        return ret + oldest_line if ret is not None else None

