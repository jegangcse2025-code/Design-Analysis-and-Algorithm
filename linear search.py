arr = [10, 25, 30, 45, 50, 65, 80]
target = 45

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element", target, "found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")