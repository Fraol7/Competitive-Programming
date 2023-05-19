class Solution:
    def evalRPN(self, List):
        stack=[]
        for element in List:
            if element in '+-*/':
                a,b=stack.pop(),stack.pop()
            if element == '+':                
                stack.append(b+a)
            elif element == '-':                
                stack.append(b-a)
            elif element == '*':                
                stack.append(b * a)
            elif element == '/':                
                stack.append(int(b/a))
            else:
                stack.append(int(element))
        return stack[0]  
    
 
    
