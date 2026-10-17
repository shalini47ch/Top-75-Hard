from collections import defaultdict
class AllOne:

    def __init__(self):
        self.hmap=defaultdict(int)

    def inc(self, key: str) -> None:
        if key in self.hmap:
            self.hmap[key]+=1
        else:
            self.hmap[key]=1
    
    def dec(self, key: str) -> None:
        #first check if the value is present in the hmap or not 
        if key in self.hmap:
            if(self.hmap[key]>1):
                self.hmap[key]-=1
            else:
                self.hmap.pop(key)
        
    def getMaxKey(self) -> str:
        if not self.hmap:
            return ""
        maxi=max(self.hmap.values())
        for key in self.hmap.keys():
            if(self.hmap[key]==maxi):
                return key
        

    def getMinKey(self) -> str:
        if not self.hmap:
            return ""
        mini=min(self.hmap.values())
        for key in self.hmap.keys():
            if(self.hmap[key]==mini):
                return key
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()