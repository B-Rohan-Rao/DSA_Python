"""
It is a function that calls itself until the condition is complete.
we can write a dummy code to understand this concept.

def open_gift_box():
    if ball:
        return ball
    open_gift_box()

The above example is the scenario where we generally prank by wrapping a gift box inside a gift box.
We cant get to the gift(Ball) until and unless a box contains a ball.
The above function will call itself until it has a ball inside it

key points ->
* The process of opening each new box(solving each new problem) is the same
* each time we open a box(solve  problem), we make the problem smaller.

"if ball:
   return ball"  <- this is a Base case (where the condition is satisfied).
If we remove this from the function, the function will keep calling itself resulting in stack overflow.

The basic example of recursion is factorial.
"""


def factorial(n):
    if n == 1:
        return 1  # <- Base Case
    return n * factorial(n - 1)


print(factorial(4))
