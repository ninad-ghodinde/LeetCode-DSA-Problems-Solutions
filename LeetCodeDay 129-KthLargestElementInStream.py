class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.arr=nums
        self.arr.sort(reverse=True)
        #self.arr=self.arr[:k]
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.arr.append(val)
        self.arr.sort(reverse=True)
        return self.arr[self.k-1]


#Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3,[4,5,8,2])
param_1 = obj.add(3)
print(param_1)