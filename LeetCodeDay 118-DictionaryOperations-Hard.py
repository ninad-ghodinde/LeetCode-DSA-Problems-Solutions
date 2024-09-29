class AllOne(object):

    def __init__(self):
        self.dict={}
    def inc(self, key):
        if key in self.dict:
            self.dict[key]+=1
        else:
            self.dict[key]=1
    def dec(self, key):
        if key in self.dict:
            self.dict[key]-=1
            if self.dict[key]==0:
                del self.dict[key]
        
    def getMaxKey(self):
        if len(self.dict)==0:
            return None
        max_val=max(self.dict.values())
        for key in self.dict.keys():
            if self.dict[key]==max_val:
                return key
    
    def getMinKey(self):
        if len(self.dict)==0:
            return None
        min_val=min(self.dict.values())
        for key in self.dict.keys():
            if self.dict[key]==min_val:
                return key  


obj = AllOne()
obj.inc("hello")
obj.dec("hello")

obj.inc("hello")

obj.inc("hello")
obj.inc("leet")
param_3 = obj.getMaxKey()
param_4 = obj.getMinKey()
print(param_3,param_4) # None None