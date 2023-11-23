def bubble_sort (list_1):
    for i in range(len(list_1)):
        for j in range(i+1, len(list_1)):
            if list_1[j] < list_1[i]:
                list_1[j], list_1[i] = list_1[i],list_1[j]
            else:
                continue
    return list_1

list_num = [5, 6, 8, 9, 1, 3,  11, 2]
print(bubble_sort(list_num))