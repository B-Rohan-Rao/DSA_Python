"""
Let's assume a list to be [4, 2, 6, 5, 1, 3]
Here, the sorting is occured by comparing two values in a list. In the above list, first 4 will be compared with 2 and will be 
replaced. Then 4 will be compared with 6. As 6 is larger than 4, the position of 4 remains unchanged and 6 is further compared 
with 5 and is replaced. This occurs until 6 finds its best postion.
it will look like this = [2, 4, 5, 1, 3, 6]
These steps are repeated further followed in Iteration 2 = [2, 4, 1, 3, 5, 6]
Iteration 3 = [2, 1, 3, 4, 5, 6]
Iteration 4 = [1, 2, 3, 4, 5, 6]
"""

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                # temp = my_list[i]
                # my_list[i] = my_list[j + 1]
                # my_list[j + 1] = temp
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


print(bubble_sort([4, 2, 6, 5, 1, 3]))
