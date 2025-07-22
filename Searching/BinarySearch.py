def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    target = 22

    print("Testing Binary Search:")
    sorted_arr = sorted(arr)  
    result = binary_search(sorted_arr, target)
    print(f"Sorted Array: {sorted_arr}")
    print(f"Target {target} found at index: {result}\n")
    
if __name__ == "__main__":
    main()