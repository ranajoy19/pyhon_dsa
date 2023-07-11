import sys

#                      2
#                     / \
#                    3    5
#                   /   /   \
#                  1    3     7
#                       \     /\
#                        4   6  8 

# lets create a helper tuple create a tree like this from left to right

max_int = sys.maxsize
min_int = -sys.maxsize-1


# tree_tuple = ((1,2,3),2,5)
# print(tree_tuple[1])




class NodeTree():
    def __init__(self,key):
        self.key =key
        self.left = None
        self.right = None
    
    @staticmethod
    def parse_tuple(data):
        if data is None:
            node =None
        elif isinstance(data,tuple) and len(data)==3:
            node = NodeTree(data[1])
            node.left = NodeTree.parse_tuple(data[0])
            node.right = NodeTree.parse_tuple(data[2])
        else:
            node= NodeTree(data)
        return node
    

    
    def __str__(self) -> str:
        return str(self.key)
# # node0 =NodeTree(2)
# # node1 =NodeTree(3)
# # node2 =NodeTree(5)

# # node0.left = node1
# # node0.right = node2

# # tree = node0

# tree =parse_tuple(tree_tuple)


# questions Tree Traversal (In , pre , post order)

# 1 Inorder Traversal - Left , Current , Right
# 2 preorder Traversal  -  Current , left , Right
# 3) Postorder Traversal - Left ,Right , Current

def inorder_traversal(node):
    if node is None:
        return []
    return inorder_traversal(node.left)+[node.key]+inorder_traversal(node.right)
    
# print(inorder_traversal(tree))

# find the height of the tree max height 

def tree_height(node):
    if node is None:
        return 0
    return 1+ max(tree_height(node.left),tree_height(node.right))

# for minimum height 

# def minDepth(tree):
#     if not tree:
#         return 0
#     elif not tree.left and not tree.right:
#         return 1
#     elif not tree.left:
#         return 1+minDepth(tree.right)
#     elif not tree.right:
#         return 1+minDepth(tree.left)
#     return 1+ min(minDepth(tree.left),minDepth(tree.right))
# print(tree_height(tree))



# find the size of the tree size of a node

def tree_size(node):
    if not node:
        return 0
    return 1+ tree_size(node.left)+tree_size(node.right)


# print(tree_size(tree))




# 2 BST (Binary Search Tree)

# A binary search tree or BST is a binary tree that satisfies the following conditions:

    # 1) The left subtree of any node only contains nodes with keys less than the node's key
    # 2) The right subtree of any node only contains nodes with keys greater than the node's key




def is_bst(node):
    return is_bstUtil(node,max_int,min_int)


def is_bstUtil(node,max,min):
    if node is None:
        return True
    
    elif  node.key< min or node.key > max:
        return False
    
    return is_bstUtil(node.left,node.key-1,min) and is_bstUtil(node.right,max,node.key+1)


    
tree = NodeTree.parse_tuple(((1, 3, None), 2, (3, 5, (6, 7, 8))))
# tree = NodeTree.parse_tuple(((1,2,3),4,5))

# print(inorder_traversal(tree))


# if is_bst(tree) is True:
#     print("Is BST")
# else:
#     print("Not a BST")



# find the value associated with given key in bst 

def find_value(tree,key):
    if tree is None:
        return None
    if tree.key == key :
        return tree
    if key < tree.key:
        find_value(tree.left,key)
    elif key>tree.key:
        find_value(tree.right,key)



