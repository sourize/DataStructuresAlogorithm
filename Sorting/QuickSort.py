def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    target = 22
    

    quicksort_arr = arr.copy()
    sorted_quick = quicksort(quicksort_arr)
    print(f"Quicksort Result: {sorted_quick}")

if __name__ == "__main__":
    main()