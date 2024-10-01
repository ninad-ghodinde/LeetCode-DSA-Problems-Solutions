class CustomStack(object):
    maxSizeGlobal=0

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSizeGlobal=maxSize
        self.myList = []*maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.myList)<self.maxSizeGlobal:
            self.myList.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.myList)<=0:
            return -1
        else:
            return self.myList.pop()
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k,len(self.myList))):
            self.myList[i]=val+self.myList[i]
                #print(self.myList[i])

        

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)