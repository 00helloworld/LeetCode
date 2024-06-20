class RandomizedSet(object):

    def __init__(self):
        self.l = []
        self.dic = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            self.l.append(val)
            self.dic[val] = len(self.l) - 1
            return True
        else:
            return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            new_index = self.dic[val]
            self.dic[self.l[-1]] = new_index  # update end value index
            self.l[-1], self.l[self.dic[val]] = self.l[self.dic[val]], self.l[-1]  # exchange to end
            self.l.pop()
            del self.dic[val]
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.l)  # No need to import, leetcode defaultly import
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
p_1 = obj.insert(0)
print(p_1)
p_2 = obj.insert(1)
print(p_2)
p_3 = obj.remove(0)
print(p_3)
p_4 = obj.insert(2)
print(p_4)
p_5 = obj.remove(1)
print(p_5)
p_6 = obj.getRandom()
print(p_6)