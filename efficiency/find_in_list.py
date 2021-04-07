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
    num_list = (1, 2, 3, 4, 5)
    print(again_in_list2((1, 2, 3, 4, 5), 4))
    