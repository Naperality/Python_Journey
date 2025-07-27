class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def InOrderTraverse(node):
    if node is None:
        return
    InOrderTraverse(node.left)
    print(node.data, end = ', ')
    InOrderTraverse(node.right)

def searchBST(node, target): # Binary search
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return searchBST(node.left, target)
    else:
        return searchBST(node.right, target)

def insertNode(node, data): # insertion
    if node is None:
        return(TreeNode(data))
    else:
        if data < node.data:
            node.left = insertNode(node.left, data)
        elif data > node.data:
            node.right = insertNode(node.right, data)
    return node

def minValue(node): # min value
    current = node
    while current.left is not None:
        current = current.left
    return current

def maxValue(node): # max value
    current = node
    while current.right is not None:
        current = current.right
    return current

def deleteNode(node, data): # delete node using the minval def
    if not node:
        return None
    if data < node.data:
        node.left = deleteNode(node.left, data)
    elif data > node.data:
        node.right = deleteNode(node.right, data)
    else:
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp

        # Node with two children, get the in-order successor
        node.data = minValue(node.right).data
        node.right = deleteNode(node.right, node.data)
    return node

# making the binary tree into BST (Binary Search Tree)
root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

# make the left less of the current node.data and right to be more
root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Traverse
InOrderTraverse(root)

# Search for a value
result = searchBST(root, 1)
if result:
    print(f"Found the node with value: {result.data}")
else:
    print("Value not found in the BST.")

# inserting node in binary tree
insertNode(root,10)
InOrderTraverse(root)

# min value and max value
minval = minValue(root)
maxval = maxValue(root)
print('\nLowest Value: ', minval.data)
print('\nHighest Value: ', maxval.data)

# deleting ndoe
deleteNode(root, 15)
InOrderTraverse(root)
