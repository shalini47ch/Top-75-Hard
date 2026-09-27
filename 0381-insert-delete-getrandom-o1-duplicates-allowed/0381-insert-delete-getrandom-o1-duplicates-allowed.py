class RandomizedCollection:

    def __init__(self):
        self.hmap=defaultdict(int)
        self.ans=[]

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            self.hmap[val]+=1
            self.ans.append(val)
            return False
        else:
            self.hmap[val]=1
            self.ans.append(val)
            return True

    def remove(self, val: int) -> bool:
        #here we have to return True if the val is present or False otherwise
        if val in self.hmap:
            if(self.hmap[val]>1):
                self.hmap[val]-=1
                self.ans.remove(val)
            else:
                self.hmap.pop(val)
                self.ans.remove(val)
            return True 
        else:
            return False

    def getRandom(self) -> int:
        n=len(self.ans)
        ele=randint(0,n-1)
        return self.ans[ele]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()