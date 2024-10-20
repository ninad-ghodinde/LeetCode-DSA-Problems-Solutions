from collections import deque


class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        st=deque()
        for curr_char in expression:
            if curr_char ==")":
                values=[]

                while st[-1]!="(":
                    values.append(st.pop())
                st.pop() #remove "("
                oprtr= st.pop() #get oprtr and remove

                result=self.evaluate_sub_expr(oprtr,values)
                st.append(result)
            elif curr_char !=",":
                st.append(curr_char) #push into stack
            
        if st[-1]=="t":
            return True
        else:
            return False
        #return st[-1]=="t"
        
    def evaluate_sub_expr(self, op, values):
        if op == "!":
            return "f" if values[0] == "t" else "t"
        
        if op == "&":
            for value in values:
                if value=="f":
                    return "f"
            return "t"
        if op == "|":
            for value in values:
                if value == "t":
                    return "t"
            return "f" 

#test cases
print(Solution().parseBoolExpr("&(|(f))")) #False
print(Solution().parseBoolExpr("!(&(f,t))")) #True
