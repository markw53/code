def bubblesort (lst):    
    swapped = False
    # Looping from size of array from last index [-1] to index [0]
    for n in range(len(lst)-1, 0, -1):
        for i in range(n):
            if lst[i] > lst[i + 1]:
                swapped = True
                # swapping data if the element if less than next element in the array
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        if not swapped:
            # exiting the function if we didn't make a simple swap
            # meaning that the array is already sorted
            return

lst = []
n = int(input('Enter number of elements: '))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)

print ("unsorted list is, ")
print (lst)
bubblesort (lst)
print ("Sorted Array is, ")
print (lst)

