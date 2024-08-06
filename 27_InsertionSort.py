"""
In this we always start from the second item in the list and compare it to the item before it. if it is smaller than the item
before it, we drop the item before it. 
For example - [4, 2, 6, 5, 1, 3]
the it will look like this in Iteration 1 - [2, 4, 6, 5, 1, 3]
Iteration 2 - No change as 6 is not less than 4
Iteration 3 - [2, 4, 5, 6, 1, 3]
Iteration 4 - [1, 2, 4, 5, 6, 3]
Iteration 5 - [1, 2, 3, 4, 5, 6]
"""

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while j >= 0 and temp < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = temp
    return my_list

print(insertion_sort([4, 2, 6, 5, 1, 3]))
    