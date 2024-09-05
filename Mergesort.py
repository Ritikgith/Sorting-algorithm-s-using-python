''''Merge sort is a popular and effictive sorting algorithm based on divide and conquer stategs. 
1. Divide and conquer 
2. Recursion
3. Merging''' 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    # yaha tb sabhi element 1 single array mai stored hai
    

    # Merge the sorted halves
    sorted_array = []
    left_index, right_index = 0, 0

    # Compare elements from left and right halves and merge them
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            sorted_array.append(left_half[left_index])
            left_index += 1
        else:
            sorted_array.append(right_half[right_index])
            right_index += 1

    # If there are remaining elements in either half, add them to the sorted array
    sorted_array.extend(left_half[left_index:])
    sorted_array.extend(right_half[right_index:])

    return sorted_array

arr=[334,35,345,23,56,23,46,76]
sorted_array=merge_sort(arr)
print("sorted array :",sorted_array)


arr=[33,45,34,56,76,32,56,54,123,43]
mid=len(arr)//2
print(mid)