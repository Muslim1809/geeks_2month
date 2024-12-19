def bubble_sort(lst):
    length_list = len(lst) - 1
    for it in range(length_list):
        for sort in range(length_list - it):
            if lst[sort] > lst[sort+1]:
                lst[sort], lst[sort+1] =lst[sort+1],lst[sort]

list1 = [42,1,44,75,94,12,3,2,8,]
print(list1)
bubble_sort(list1)
print(list1)