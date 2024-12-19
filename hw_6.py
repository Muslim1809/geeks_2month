def binary_search(a,value):
    n = len(a)
    first = 0
    last = n - 1
    middle = n // 2
    result = False
    while a[middle] != value and first <= last:
        if value > a[middle]:
            first = middle + 1
        else:
            last = middle - 1
        middle = (first + last) // 2
    if value == a[middle]:
        result = True

    if result == True:
        #ID Это индекс элемента в списке
        print(f"id of {value} == {middle}")
    else:
        print('No value')
lst = [6, 17, 21, 27, 32, 34, 34, 36, 37, 48]
print(lst)
binary_search(lst,34)
binary_search(lst,11)