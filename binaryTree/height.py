from BinaryTree import TreeNode

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)

def height(node):
    if not node:
        return 0
    left_h = height(node.left)
    right_h = height(node.right)
    if left_h > right_h:
        return left_h + 1
    else:
        return right_h + 1

h = height(tree)
print(h)
