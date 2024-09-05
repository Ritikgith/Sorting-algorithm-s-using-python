

import timeit # use to find the code exicution time...

arry=[3,5,23,13,67]
def bubble_sort(arry):
    n=len(arry)
    #Step 1: Loop through each element in the array..
    for i in range(n):
        #Step 2: Last i elements are already sorted..
        for j in range(0,n-i-1): # becouse array ka last element correct position pai he rhega...
            #step 3: Compare adjacent elements..
            if arry[j]>arry[j+1]:
                #Step 4: Swap if they are in the wrong order..
                arry[j],arry[j+1]=arry[j+1],arry[j]
                
bubble_sort(arry)
print(timeit.timeit(lambda : bubble_sort(arry.copy()),number=(1000)))