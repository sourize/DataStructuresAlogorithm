def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():

    arr = [64, 34, 25, 12, 22, 11, 90]
    target = 22
    

    insertion_arr = arr.copy()
    insertion_sort(insertion_arr)
    print(f"Insertion Sort Result: {insertion_arr}")
    

if __name__ == "__main__":
    main()