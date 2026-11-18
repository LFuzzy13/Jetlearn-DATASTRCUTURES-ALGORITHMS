def search(root, key):

    root = Node(10)

    root.left = Node(5)
    root.right = Node(15)

    root.left.left = Node(2)
    root.left.right = Node(7)

    root.right.left = Node(12)
    root.right.right = Node(20)
    
    if root is None:
        return False


    if root.data == key:
        return True

 
    return search(root.left, key) or search(root.right, key)