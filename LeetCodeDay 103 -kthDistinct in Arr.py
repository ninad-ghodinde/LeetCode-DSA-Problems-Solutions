class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        freq={}
        for ar in arr:
            if ar in freq:
                freq[ar]+=1
            else:
                freq[ar]=1
        arrList=[]
        for key in freq:
            if freq[key]==1:
                arrList.append(key) 
        print(arrList)
        if k>len(arrList):
            return ""
        else:
            return arrList[k-1]


print(Solution().kthDistinct( ["d","b","c","b","c","a"], k = 2)) # Expected output: a