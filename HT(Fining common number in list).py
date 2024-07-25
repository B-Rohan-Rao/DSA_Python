# list1 = [1, 3, 5]
# list2 = [2, 4, 5]


# Approach 1-> Using nested Loops
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


# This has the time complexity of O(n^2) as it has nested loop

# Approach 2-> Using Dictionary
def item_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True

    return False


# This has a time complexity of O(n). It is initially O(2n) as there are 2 loops, but we drop the constant.
# Approach 2 is more efficient.


list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))
print(item_common(list1, list2))
