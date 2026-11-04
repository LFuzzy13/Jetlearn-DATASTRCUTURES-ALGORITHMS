class Tree:
    def __init__ (self,data):
        self.data = data
        self.left_node = None
        self.right_node = None

def inordertraversal (root):
    if root.left_node !=None:
        inordertraversal(root.left_node)
    print(root.data)
    if root.right_node !=None:
        inordertraversal(root.right_node)

def preordertraversal (root):
    print(root.data)
    if root.left_node !=None:
        preordertraversal(root.left_node)
    if root.right_node !=None:
            preordertraversal(root.right_node)
    
def postordertraversal (root):
    if root.left_node !=None:
            preordertraversal(root.left_node)
    if root.right_node !=None:
            preordertraversal(root.right_node)
    print(root.data)

def DisplayTree(root, prefix="", isLeft = True):
    if root == None:
        return
    print(prefix + ("|----" if isLeft else "L----") + str(root.data))

    if root.left_node !=None:
        DisplayTree(root.left_node, prefix + ("|   "if isLeft else "    "), True)
    if root.right_node !=None:
        DisplayTree(root.right_node, prefix + ("|   "if isLeft else "    "), True)
    

root = Tree(int(input("Enter The Root Node: ")))

root.left_node = Tree(int(input("Enter The Left Child: ")))
root.right_node = Tree(int(input("Enter The Right Child: ")))

root.left_node.left_node = Tree(int(input("Enter The Left Child Of Left Node: ")))
root.left_node.right_node = Tree(int(input("Enter The Right Child Of Left Node: ")))

root.right_node.left_node = Tree(int(input("Enter The Left Child Of Right Node: ")))
root.right_node.right_node = Tree(int(input("Enter The Right Child Of Right Node: ")))


print(root.data)
DisplayTree(root.left_node,"",True)
DisplayTree(root.right_node,"",False)

print("Inorder Traversal")
inordertraversal(root)
print("--------")
print("Preorder Traversal")
preordertraversal(root)
print("--------")
print("Postorder Traversal")
postordertraversal(root)
print("--------")
print("Traversal Complete.")