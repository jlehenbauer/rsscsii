import timeit

def find_in_list(num_list, num):
    if num in num_list:
        return True
    else:
        return False
def again_in_list(num_list, num):
    checker = 0
    for x in num_list:
        if x == num:
            checker+=1
        else:
            checker+=0
    if checker > 0:
        return True
    else:
        return False

def again_in_list2(num_list, num):
    checker = 0
    for x in num_list:
        if x == num:
            return True
    return False

if __name__=="__main__":
    num = 4
    num_list = [1, 2, 3, 4, 5]
    # Find in list
    print(f"find_in_list({num_list}, {num}):")
    print(timeit.timeit("find_in_list([1, 2, 3, 4, 5], 4)", "from __main__ import find_in_list"))
    
    # Again in list
    print(f"again_in_list({num_list}, {num}):")
    print(timeit.timeit("again_in_list([1, 2, 3, 4, 5], 4)", "from __main__ import again_in_list"))
    
    # Again in list 2
    print(f"again_in_list2({num_list}, {num}):")
    print(timeit.timeit("again_in_list2([1, 2, 3, 4, 5], 4)", "from __main__ import again_in_list2"))
    