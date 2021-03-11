# Paul Christman (Student ID: 001524778)
class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item


class HashMap:

    # Constructor
    # Space-time complexity O(1)
    def __init__(self, capacity=10):
        self.map = []
        for i in range(capacity):
            self.map.append([])

    # Creates a new hash key for a package
    # Space-time complexity of O(1)
    def create_hash(self, key):
        return int(key) % len(self.map)

    # Insert a new package into the hash table
    # Space-time complexity of O(N)
    def insert(self, key, value):
        key_hash = self.create_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Update a package that is in the hash table
    # Space-time complexity of O(N)
    def update(self, key, value):
        key_hash = self.create_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print(f"There was an error with updating on key: {key}")

    # Retrieves a value from the hash table
    # Space-time complexity of O(N)
    def get_value(self, key):
        key_hash = self.create_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Removes a value from the hash table
    # Space-time complexity is O(N)
    def delete(self, key):
        key_hash = self.create_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False
