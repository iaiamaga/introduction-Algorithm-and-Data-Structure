def recrsive_binary_search(list, tagert):
    if len(list) == 0:
        return False
    else: 
        midpoint = (len(list)) // 2
        
        if list[midpoint] == tagert:
            return True
        
        else:
            if list[midpoint] < tagert:
                return recrsive_binary_search(list[midpoint + 1:], tagert)
            else:
                return recrsive_binary_search(list[:midpoint], tagert)

def verify(result):
    print("Target found:", result)
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recrsive_binary_search(numbers, 6)
verify(result)

result = recrsive_binary_search(numbers, 16)
verify(result)