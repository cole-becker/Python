# INSERT YOUR IMPLEMENTATION OF binary_search HERE
def binary_search(values, to_find, start_index, end_index, count=0):
    
    count += 1
    if start_index > end_index:
        return count, False
    
    middle = (start_index + end_index) // 2

    count += 1
    if values[middle] == to_find:
        return count, True
    
    count += 1
    if values[middle] > to_find:
        return binary_search(values, to_find, start_index, middle - 1, count)
    
    else:
        return binary_search(values, to_find, middle + 1, end_index, count)
    