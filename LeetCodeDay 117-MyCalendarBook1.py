class MyCalendar(object):

    def __init__(self):
        self.calendar =[]
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """    
        for s,e in self.calendar:
            if start<e and end >s:
                return False
        self.calendar.append((start,end))
        print(self.calendar)
        return True
        
        


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
param_1 = obj.book(10,20)
print(param_1)
param_2 = obj.book(15,25)

print(param_2)