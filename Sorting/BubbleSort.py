def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    
    arr = []
    a = int (input("Enter the no. of elements: "))
    for i in range (a):
        ae = int(input("Enter the values: ")) 
        arr.append(ae)
        
#arr = [64, 34, 25, 12, 22, 11, 90]

    
    bubble_arr = arr.copy()
    bubble_sort(bubble_arr)
    print(f"Bubble Sort Result: {bubble_arr}")

if __name__ == "__main__":
    main()