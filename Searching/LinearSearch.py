def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    target = 22


    print("Testing Linear Search:")
    result = linear_search(arr, target)
    print(f"Array: {arr}")
    print(f"Target {target} found at index: {result}\n")
    

if __name__ == "__main__":
    main()