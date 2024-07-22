num1 = 11
num2 = num1

print("Before    num2 is updated")
print("the value of num1 is", num1)
print("the value of num2 is", num2)

print("\n num1 points to", id(num1))
print("\n num2 points to", id(num2))

num2 = 22
print("after num2 is updated")
print("the value of num1 is", num1)
print("the value of num2 is", num2)

print("\n num1 points to", id(num1))
print("\n num2 points to", id(num2))
