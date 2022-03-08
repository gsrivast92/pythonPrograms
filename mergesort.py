def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid_index = len(arr) //2
    mid_element = arr[mid_index]
    left_arr= arr[:mid_index]
    right_arr = arr[mid_index:]
    
    merge_sort(left_arr)
    merge_sort(right_arr)
    
    merge_two_sorted(left_arr,right_arr, arr)
    
    
    
    


def merge_two_sorted(left,right,arr):
    sorted_list = []
    i = j= k=0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i +=1
        
        else:
            arr[k] = right[j]
            j +=1
        k +=1
            
    while i < len(left):
        arr[k] =left[i]
        i +=1
        k +=1
    while j < len(right):
        arr[k] =right[j]
        i +=1
        k +=1
    
        

        
    