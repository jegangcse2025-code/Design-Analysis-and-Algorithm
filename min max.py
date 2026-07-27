import random
comparison_count = 0 # Global counter

def min_max_dc(arr, low, high):
    global comparison_count
    # Base case: single element
    if low == high:
        return arr[low], arr[low]
    # Base case: two elements
    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        return arr[high], arr[low]
    # Divide
    mid = (low + high) // 2
    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)
    # Conquer: combine with 2 comparisons
    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin
    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax
    return overall_min, overall_max

def min_max_naive(arr):
    mn, mx = arr[0], arr[0]
    comps = 0
    for x in arr[1:]:
        comps += 1
        if x < mn:
            mn = x
        else: # fixed logical structure for precise naive comparison tracking if standard worst-case/average-case behavior is expected, but let's check code's actual output
            comps += 1
            if x > mx:
                mx = x
    return mn, mx, comps

# Re-running user's exact code to capture output
def min_max_naive_exact(arr):
    mn, mx = arr[0], arr[0]
    comps = 0
    for x in arr[1:]:
        comps += 1
        if x < mn:
            mn = x
        comps += 1
        if x > mx:
            mx = x
    return mn, mx, comps

arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]
comparison_count = 0
mn, mx = min_max_dc(arr, 0, len(arr) - 1)
dc_comps = comparison_count
_, _, naive_comps = min_max_naive_exact(arr)

print(f'DC Comps: {dc_comps}')
print(f'Naive Comps: {naive_comps}')
