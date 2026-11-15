n = [12, -1, -7, 8, -15, 30, 16, 28]
w = 3

def first_negative_subarray(arr, k):
    i = 0
    j = 0
    fn = []
    result = []

    while j < len(arr):
        if arr[j] < 0:
            fn.append(arr[j])
        
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if fn:
                result.append(fn[0])
            else:
                result.append(0)
            
            # Only remove if arr[i] is equal to the first negative
            if fn and arr[i] == fn[0]:
                fn.pop(0)
            
            i += 1
            j += 1

    return result

mx = first_negative_subarray(n, w)
print(mx)
