# Just to understand the concept of linkedlist
# LinedList can also be Understood as a dict. that contains other dict.
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

print(head['next']['next']['value'])
