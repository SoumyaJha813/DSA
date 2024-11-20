class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    if root is None: # check to prevent infinite runtime error
        return
    d = {}
    def traverse(root, h, l):
        if root is None:   # check to prevent infinite runtime error
            return
        if root:
            if h not in d or d[h][1]>l:  #if h is not in dictionary or level of cuurent node is more than the previous then add to dict.
                d[h] = [root.info,l]   # here height is the key {h: [root, l]} and it's root value and level is value in form of a list
        traverse(root.left,h-1,l+1)  # as the level increase and left side of root the height descreses
        traverse(root.right,h+1,l+1)  # as the level increases and right side of the root the height increases
    traverse(root,0,0)
    
    for h in sorted(d.keys()):  # sort the elements like using height(key) of a node.
        print(d[h][0], end = " ")
        
        

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
