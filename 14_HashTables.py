# Hash Tables can be said as a method or mapping technique that uses the O(1) for storing or retrieving Data
# A build In hash Table's example can be given as Dictionaries in python, Hash DS also uses key value pair

# Terminologies
# Search Keys -> The values or keys through which we can get the data
# Hash Table -> The data structure that stores the data, It uses the hash function to retrieve data in order of O(1)
# Hashing Techniques -> Static Background DS: uses Arrays, Dynamic Background DS: uses Linkedlist


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * 7

    # Hash Method.
    def __hash(self, key):  # Key parameter is passed to determine the address where we have stored that key-value pair
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            # ord() gives the ASCII character for any character we pass. and 23 is multiplied as it is a prime number.
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_items(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.get_items('bolts'))
print(my_hash_table.get_items('washers'))
print(my_hash_table.get_items('lumber'))
print(my_hash_table.get_items('screw'))

my_hash_table.print_table()
print(my_hash_table.keys())
