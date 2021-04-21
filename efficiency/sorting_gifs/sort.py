import random
from timeit import timeit

def insertion_sort(in_list):
    new_list = [in_list[0]]
    for i in in_list[1:]:
        nl_len = len(new_list)
        if i < new_list[0]:
            new_list = [i] + new_list
            #print (new_list)
        else:
            for j in range(len(new_list)):
                if i < new_list[j]:
                    new_list = new_list[:j] + [i] + new_list[j:]
                    #print (new_list)
                    break
            if len(new_list) == nl_len:
                new_list.append(i)
                #print (new_list)
    return new_list


def bubble_sort(my_list):
    if len(my_list) == 1:
        return my_list
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            hold = my_list[i+1]
            my_list[i+1] = my_list[i]
            my_list[i] = hold
    return bubble_sort(my_list[:-1]) + [my_list[-1]]


def check_low(my_list):
    low = my_list[0]
    for x in my_list[1:]:
        if x < low:
            low = x
    return low

    
def selection_sort(unsorted):
    new_sorted = []
    while unsorted != []:
        new_sorted.append(check_low(unsorted))
        unsorted.remove(new_sorted[-1])
    return new_sorted


def list_gen(low, high):
    gen_list = list(range(low, high+1, 1))
    random.shuffle(gen_list)
    #print(gen_list)
    return gen_list

mega_list = [insertion_sort, bubble_sort, selection_sort]
if __name__ == "__main__":
    fin_list = list_gen(1, 10)
    print(f"sorting list: {fin_list}")
    
    '''
    for x in mega_list:
        print("-----------------------------")
        print(x(fin_list))
        print("-----------------------------"
    '''
    print("inserion_sort")
    print(timeit("insertion_sort(" + str(fin_list) +")", "from __main__ import insertion_sort", number=300000))
    
    print("bubble_sort")
    print(timeit("bubble_sort(" + str(fin_list) +")", "from __main__ import bubble_sort", number=300000))
    
    print("selection_sort")
    print(timeit("selection_sort(" + str(fin_list) +")", "from __main__ import selection_sort", number=300000))
        