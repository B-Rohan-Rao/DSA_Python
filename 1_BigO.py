def print_number(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_number(10)

"""
For above, the loops are running independently so it will be O(n)
For next example, we can see nested loop resulting in O(n^2)
"""

def print_number(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


print_number = 10
