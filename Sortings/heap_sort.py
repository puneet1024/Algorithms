#HEAP SORT

#Heap Sort is an in-place sorting algorithm
#Step1 : Build a max heap from the arbitary array
#Step2 : Swap root element with the last element
#Step3 : Heapify again by making a max heap

def heapify(arr,i,n):
    largest = i
    #Left child l
    l = 2 * i + 1
    #R=ight child r
    r = 2 * i + 2

    #Check if left child occurs and it is greater than root
    if ( l < n and arr[i] < arr[l]):
        largest = l

    #Check if right child exists and it is greater than left and root
    if (r < n and arr[largest] < arr[r]):
        largest = r

    #If root not largest, swap the root element with the largest
    if largest != i :
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,largest,n)

def heapSort(arr):
    #n is the length of the array
    n = len(arr)

    #Step1
    #max heap starting from bottom up
    for i in range(n,0,-1):
        heapify(arr,i,n)

    #Step2
    #Swapping first and last element
    for j in range(n-1,0,-1):
        arr[j],arr[0] = arr[0],arr[j]
        #Step3
        #Build a max heap after every swapping
        #Top Down heapify
        heapify(arr,0,j)    #0 because we start from root and till j because elements after j are already sorted


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
heapSort(arr)
for i in range(n):
    print(arr[i])

