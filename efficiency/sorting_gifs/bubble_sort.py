
def bubble_sort(my_list):
    if len(my_list) == 1:
        return my_list
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            hold = my_list[i+1]
            my_list[i+1] = my_list[i]
            my_list[i] = hold
    return bubble_sort(my_list[:-1]) + [my_list[-1]]
    
print(bubble_sort([4, 1, 6, 3, 8, 2, 5, 7]))