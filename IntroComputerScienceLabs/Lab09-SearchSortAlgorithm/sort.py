# ADD YOUR IMPLEMENTATION OF insertion_sort HERE
def insertion_sort(arr):
    count = 0
    for j in range(1, len(arr)):
        key = arr[j]
        count += 1
        i = j - 1
        while i >= 0 and arr[i] > key:
            count += 1
            if arr[i] > key:
                count += 1
                arr[i + 1] = arr[i]
                i -= 1
            
            else:
                count += 1
        
        count += 1
        arr[i + 1] = key
    
    return arr, count
