#sutdent mark system

class SMark:
    def __init__(self,x):
        self.data = x
        self.leftChild = None
        self.rightChild = None
def InOrderTraversal(root):
    if root is not None:
        if root.leftChild is not None:
            InOrderTraversal(root.leftChild)
        print(root.data)
        if root.rightChild is not None:
            InOrderTraversal(root.rightChild)
def Insert(root,k):
    if root ==None:
        return SMark(k)
    if root.data > k:
        root.leftChild = Insert(root.leftChild,k)
    else:
        root.rightChild = Insert(root.rightChild, k)
        return root
    
def Search(root,key):
    if root.data ==key:
        return root
    elif root.data > key and root.leftChild is not None:
        return Search(root.leftChild,key)
    elif root.data < key and root.rightChild is not None:
        return Search (root.rightChild, key ) 
    else: 
        return -1

n = int(input("Enter how many students - "))
root = None
for i in range(n):
    x = input("Enter student name and mark -")
    root = Insert(root,x)

InOrderTraversal(root)
key = input("Enter student name and mark to search - ")
keyNode = Search(root,key)
if keyNode == -1:
    print("Student not found")
else:
    print("Student Mark", keyNode.data)
