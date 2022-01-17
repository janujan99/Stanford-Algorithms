class HashTable:
    def __init__(self) -> None:
        self.lst = [0]*1000
        self.population = 0

    def hash_function(self, x):
        return (9895275179*x) % len(self.lst)

    def add(self, key, item):
        index = self.hash_function(key)

        while self.lst[index]:
            index += 1
            if index == len(self.lst):
                index = 0

        self.lst[index] = (key, item)
        self.population +=  1

        return

    def delete(self, key):
        index = self.hash_function(key)
        found = True

        while self.lst[index] != 0 and self.lst[index][0] != key:
            index += 1
            if index == len(self.lst):
                index = 0
            if self.lst[index] == 0:
                print("Item not found...")
                found = False

        if found:
            self.lst[index] = None
            self.population -= 1

        return

    def get(self, key):
        index = self.hash_function(key)
        found = True

        while self.lst[index] and self.lst[index][0] != key:
            index += 1
            if index == len(self.lst):
                index = 0
            if self.lst[index] == 0:
                print("Item not found...")
                found = False

        if found and self.lst[index]:
            return self.lst[index][1]

        return None
