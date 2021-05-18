### Merge Sort ### MERGE SORT ONLY WORKSF FOR SORTED ARRAYS !!!

def merge(arr1, arr2): # Takes two sorted arrays
    results = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr2[j] > arr1[i]:                            # arr1 = [10,24,72] arr2 = [1,9,76] res = [1,9,10,24,72,76]      i = 2, j = 3
            results.append(arr1[i])
            i += 1
        else:
            results.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        results.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        results.append(arr2[j])
        j += 1
    
    #print(results)
    return results

#merge([1,10,50], [2,14,99,100])


#Every recursive function has a base case and a recursive case.

def mergeSort(arr):
        if len(arr) <= 1:
            return arr
        mid = round(len(arr)/2)
    
        left = mergeSort(arr[0:mid])
        right = mergeSort(arr[mid:])
    
        print(merge(left, right))
        return merge(left, right)


mergeSort([10,24,76,72,1,9])

