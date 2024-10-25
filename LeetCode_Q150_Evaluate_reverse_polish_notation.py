class Solution:
    def operation(self,op1: int, op2: int, op: str) -> int:
        if op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            return int(op1 / op2)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','*','/']
        resVal = 0
        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            elif tok in operators:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                resVal = self.operation(operand1,operand2,tok)
                stack.append(resVal)
        return stack.pop()
    
