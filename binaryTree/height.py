import TreeNode

def height(node):
    if not node:
        return 0
    left_h = height(node.left)
    right_h = height(node.right)
    if left_h > right_h:
        return left_h + 1
    else:
        return right_h + 1
