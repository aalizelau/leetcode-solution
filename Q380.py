import random

class RandomizedSet(object):

    def __init__(self):
        self.data_map = {}  
        self.data_list = []

    def insert(self, val):
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data_list)
        self.data_list.append(val)
        return True
        

    def remove(self, val):
        if val not in self.data_map:
            return False
        index = self.data_map[val]
        last_element = self.data_list[-1]

        self.data_list[index] = last_element
        self.data_map[last_element] = index

        self.data_list.pop()
        del self.data_map[val]

        return True
        

    def getRandom(self):
        return random.choice(self.data_list)
        


