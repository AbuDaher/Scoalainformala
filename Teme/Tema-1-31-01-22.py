my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_sorted_list = sorted(my_list)
print(my_sorted_list)
my_sorted_list.reverse()
print(my_sorted_list)
my_sliced_list_1 = my_sorted_list[::2]
print(my_sliced_list_1)
my_sliced_list_2 = my_sorted_list[1::2]
print(my_sliced_list_2)
my_sliced_list_3 = my_sorted_list[1:-2:3]
print(my_sliced_list_3)