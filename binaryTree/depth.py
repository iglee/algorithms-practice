from BinaryTree import TreeNode

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)

def assign_level(node):
    flat_tree = []
    level = 0

    q = [node]

    while q:
        count = len(q)

        while count > 0: 
            n = q.pop(0)
            flat_tree.append((n.val, level))

            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
            count -= 1

        level += 1
    return flat_tree

level = assign_level(tree)
print(level)

