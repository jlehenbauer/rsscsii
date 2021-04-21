
def check_low(my_list):
    low = my_list[0]
    for x in my_list[1:]:
        if x < low:
            low = x
    return low
    
def selection_sort():
    unsorted = [3, 8, 2, 5, 7, 1, 4, 6]
    new_sorted = []
    while unsorted != []:
        new_sorted.append(check_low(unsorted))
        unsorted.remove(new_sorted[-1])
    return new_sorted
    

