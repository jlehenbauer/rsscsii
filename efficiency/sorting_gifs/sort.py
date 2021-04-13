def insertion_sort(in_list):
    new_list = [in_list[0]]
    for i in in_list[1:]:
        for j in range(len(new_list)):
            if i < new_list[j]:
               new_list = new_list[:j-1] + [i] + new_list[j:]
            break
    return [new_list]

if __name__ == "__main__":
    print(insertion_sort([2, 6, 1, 3, 8, 5, 4, 7]))
