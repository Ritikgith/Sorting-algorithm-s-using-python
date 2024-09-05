'''start at the beginning -- begin with the first element of array
2. scan through the entire aray (or the unsorted portion) to find the smallest element..
3. swap this smallest element with the first element of the unsorted portion of the array...
4.move the boundary of the sorted portion one element to the right..
5. repeat steps 2-4 for the remaining unsorted portion until the entire array is sorted..
'''
'''get start'''
arry=[44,32,6,23,12,556,89,55,43,123,76,67]

def selection_sort(arry):
    for i in range(0,len(arry)-1):
        curr_min=i
        for j in range(i+1,len(arry)):
            if arry[j]<arry[curr_min]:
                curr_min=j
        arry[i],arry[curr_min]=arry[curr_min],arry[i]

selection_sort(arry)
print(arry)


# for i in range(1,11):
#     print(i)
    
    
    
i =1
while i<=11:
    print(i)
    i+=1
    
    
    
arr=[33,23,55,44,12,67,34,23,45,444,876]

def selection_sort(arr):
    for i in range(0,len(arr)):
        min_value=i
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
selection_sort(arr)
print(arr)
