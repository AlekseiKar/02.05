def pair_insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
        
        if j % 2 == 0:
            k = j - 1
        else:
            k = j + 1
            
        while k >= 0 and arr[k] > arr[k+1]:
            arr[k], arr[k+1] = arr[k+1], arr[k]
            if k > 0:
                k -= 2
            else:
                k -= 1
                
    return arr

# Пример использования
arr = [4, 2, 1, 3, 6, 5]
result = pair_insertion_sort(arr)
print(result)
