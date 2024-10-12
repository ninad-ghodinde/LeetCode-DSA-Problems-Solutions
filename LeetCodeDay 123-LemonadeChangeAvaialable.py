class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change_5=0
        change_10=0
        for bill in bills:
            if bill == 5:
                change_5+=1 #add to change
            elif bill ==10:
                if change_5 > 0: #to give 5 change back
                    change_5 -=1
                    change_10 +=1
                else:
                    return False #cant give change
            else:
                if change_5 >0 and change_10>0:
                    change_5 -=1
                    change_10 -=1
                elif change_5>=3:
                    change_5 -=3
                else:
                    return False
        return True

# test
print(Solution().lemonadeChange([5,5,10,10,20])) # False
print(Solution().lemonadeChange([5,5,5,10,20])) # True