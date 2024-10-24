class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        characters = path.split('/')
        for char in characters:
            if char == '.' or char == '' :
                continue
            elif char == '..':
                if stack:
                    stack.pop()
            else:
                print(char)
                stack.append(char)
        return '/'+ '/'.join(stack)
