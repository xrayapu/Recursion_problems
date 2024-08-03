#problem 2: hight of a binary tree.
class Node:
    def __init__(self,val) :
        self.left=None
        self.right=None
        self.val= val

# main code is here
def sol(node):
    if not node:
        return 0
    
    left= sol(node.left)
    right= sol(node.right)
    #print(left,right)
    return max(left,right)+1
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)

print(sol(root))
