class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_open = ['(','{','[']
        brackets_close = [')','}',']']
        for oper in s:
            if oper in brackets_open:
                stack.append(oper)
            elif oper in brackets_close:
                if stack and ((oper == ')' and stack[-1] == '(') or(oper == '}' and stack[-1] == '{') or (oper == ']' and stack[-1] == '[') ):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
