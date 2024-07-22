dict1 = {"value": 11}
dict2 = dict1

print("Before updating the dict2")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("/n dict2 points to", id(dict1))
print("/n dict2 points to", id(dict2))
dict2["value"] = 22

print("After updating the dict2")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("/n dict2 points to", id(dict1))
print("/n dict2 points to", id(dict2))
