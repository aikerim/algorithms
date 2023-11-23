def binary_search(list_2, value):
    result = False
    first = 0
    last = len(list_2)
    pos = 0
    while first < last:
        middle = (first+last)//2
        if value == list_2[middle]:
            first = middle
            last = first
            result = True
            pos = middle
        elif value > list_2[middle]:
            first = middle+1
        else:
            last = middle-1       
    if result == True:
        print(f"Элемент найден, индекс элемента {value} - {pos}")
    else:
        print("Элемент не найден")

list_n = [1, 2, 3, 5, 8, 11, 22, 23, 40]
val = 11
binary_search(list_n, val)