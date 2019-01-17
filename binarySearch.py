# This program binary search method in python

def binary_search(arr, f, l, v, sorted_ar = False):
    if not sorted_ar:
        arr.sort()
    if l-f < 0:
        return -1        
    else:
        mid_element_i = (f+l) // 2
        if arr[mid_element_i] == v:
            return mid_element_i
        elif v > arr[mid_element_i]:
            return binary_search(arr, mid_element_i+1, l, v, True)
        else:
            return binary_search(arr, f,  mid_element_i-1, v, True)        




test = [10, 19, 28, 29, 37, 38, 46, 47, 50, 56]
q = int(input("\nSearch:"))
print("Result:")
find_i = binary_search(test, 0, len(test)-1, q, False)
if (test[find_i] == q ):
    print(" Found[{}] at index({}) in test array".format(q, find_i))
else:
    print(" No results for [{}] in test array. Try another search ! ".format(q))        