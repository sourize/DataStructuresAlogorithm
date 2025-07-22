def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():

    arr = [64, 34, 25, 12, 22, 11, 90]
    target = 22
    

    selection_arr = arr.copy()
    selection_sort(selection_arr)
    print(f"Selection Sort Result: {selection_arr}")


if __name__ == "__main__":
    main()
