"""
my_list = [1, 2, 3, 4, 5, 6]
Here we are going to look at the index. 
In iteration 1, since 4 is the first value that we have seen yet, min_index = 0
Further, since 2 is the smaller than 4, min_index = 1
Further, since 1 is the smaller than 2, min_index = 4
Then when we get the min. value and it's index, we are going to switch. It should be noted that we are storing the index and 
not the value in min_index.
It should look like this = [1, 2, 6, 5, 4, 3]
Iteration 2 = No change because two is the min value.
Iteration 3 = [1, 2, 3, 5, 4, 6]
Iteration 4 = [1, 2, 3, 4, 5, 6]
"""
def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list

print(selection_sort([4, 2, 6, 5, 1, 3]))
