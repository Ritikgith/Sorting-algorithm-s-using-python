# arry=[44,32,6,23,12,556,89,55,43,123,76,67]

# def insertion_sort(arry):
#     for i in range(1,len(arry)):
#         j=i
#         while arry[j-1]>arry[j] and j>0:
#             arry[j-1],arry[j]=arry[j],arry[j-1]
#             j-=1
# insertion_sort(arry)
# print("sorted array is : ",arry)





arr=[34,345,23,44,65,78,22,43]
def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(1,len(arr)):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
insertion_sort(arr)
print(arr)

#hello ritik..