class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        x=y=0

        for val in tokens:
            if val=="+":
                stack.append(stack.pop()+stack.pop())
            elif val=="-":
                x=stack.pop()
                y=stack.pop()
                stack.append(y-x)
            elif val=="*":
                stack.append(stack.pop()*stack.pop())
            elif val=="/":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(val))

        return stack[0]