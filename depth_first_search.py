class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):
    if not root:
        return
    
    print(root.val)
    dfs(root.left)
    dfs(root.right)
    
root = TreeNode(1)
left1 = TreeNode(2)
root.left = left1

right1 = TreeNode(3)
root.right = right1


left2 = TreeNode(4)
right2 = TreeNode(5)

left1.left = left2
left1.right = right2

left3 = TreeNode(6)
right3 = TreeNode(7)

right1.left = left3
right1.right = right3

dfs(root)
