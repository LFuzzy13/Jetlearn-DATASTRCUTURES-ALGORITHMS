#opencv test tree

import cv2
import numpy as np
import time


class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def InorderTraversal(root):
    if root == None:
        return []

    return InorderTraversal(root.leftNode)+[root]+ InorderTraversal(root.rightNode)

def PreorderTraversal(root):
    if root == None:
        return []
    return [root]+PreorderTraversal(root.leftNode)+PreorderTraversal(root.rightNode)

def PostorderTraversal(root):
    if root == None:
        return []
    return PostorderTraversal(root.leftNode)+PostorderTraversal(root.rightNode)+[root]

def DrawTree(root,positions,visited,current,sequence,title):
    img = np.ones((650,900,3),dtype=np.uint8)*245
    cv2.putText(img,title,(230,45),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,0),2)
    def draw_lines(node):
        if node == None:
            return
        x1,y1=positions[id(node)]
        if node.leftNode !=None:
            x2,y2=positions[id(node.leftNode)]
            cv2.line(img,(x1,y1),(x2,y2),(0,0,0),3)
            draw_lines(node.leftNode)

        if node.rightNode !=None:
            x2,y2 = positions[id(node.rightNode)]
            cv2.line(img,(x1,y1),(x2,y2),(0,0,0),3)
            draw_lines(node.rightNode)
    draw_lines(root)

    def draw_nodes(node):

        if node == None:
            return

        x,y = positions[id(node)]

        if node == current:
            color = (0,200,255) # yellow : current node

        elif id(node) in visited:
            color = (0,200,0) # green : visited node

        else:
            color = (255,150,100) # blue : not visited

        cv2.circle(img,(x,y),30,color, -1)
        cv2.circle(img,(x,y),30,(0,0,0),2)

        cv2.putText(
            img,
            str(node.data),
            (x-12,y+8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,0,0),
            2,
        )
        draw_nodes(node.leftNode)
        draw_nodes(node.rightNode)
    draw_nodes(root)

    cv2.putText(
        img,
        "Traversal Sequence",
        (50,500),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,0,0),
        2,
    )
    sequence_text = " -> ".join(map(str, sequence))
    cv2.putText(
        img, sequence_text, (50,540), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,0,150), 2
    )

    cv2.circle(img,(70,600),10,(255,150,100),-1)
    cv2.putText(
        img,"Not Visited",(90,606), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1
    )

    cv2.circle(img,(300,600),10,(0,200,255),-1)
    cv2.putText(img,"Current",(320,606),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)

    cv2.circle(img,(500,600),10,(0,200,0),-1)
    cv2.putText(img,"Visited",(520,606),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)

    cv2.imshow("Tree Traversal Visualizer", img)

def AnimateTraversal(root,traversal, title, positions):

    visited = set()
    sequence = []

    for node in traversal:
        DrawTree(root,positions,visited, node, sequence,title)
        key = cv2.waitKey(1000)

        if key == ord("q"):
            return False

        visited.add(id(node))
        sequence.append(node.data)

    DrawTree(root,positions,visited,None,sequence,title)

    cv2.waitKey(2000)
    return True

root = TreeNode(int(input("Enter Root Node")))
root.leftNode = TreeNode(int(input("Enter The Left Child: ")))
root.rightNode = TreeNode(int(input("Enter The Right Child: ")))

root.leftNode.leftNode = TreeNode(int(input("Enter The Left Child Of Left Node: ")))
root.leftNode.rightNode = TreeNode(int(input("Enter The Right Child Of Left Node: ")))

root.rightNode.leftNode = TreeNode(int(input("Enter The Left Child Of Right Node: ")))
root.rightNode.rightNode = TreeNode(int(input("Enter The Right Child Of Right Node: ")))


positions = {
    id(root):(450,120),
    id(root.leftNode): (250,270),
    id(root.rightNode):(650,270),
    id(root.leftNode.leftNode):(150,420),
    id(root.leftNode.rightNode):(350,420),
    id(root.rightNode.leftNode): (550,420),
    id(root.rightNode.rightNode): (750,420),
}


inorder = InorderTraversal(root)
preorder = PreorderTraversal(root)
postorder = PostorderTraversal(root)

cv2.namedWindow("Tree Traversal Visualizer")
print("Press Q to stop the animation.")

AnimateTraversal(root,inorder,"INORDER : LEFT -> ROOT -> RIGHT", positions)
AnimateTraversal(root,preorder,"PREORDER : ROOT -> LEFT -> RIGHT", positions)
AnimateTraversal(root,postorder,"POSTORDER : LEFT -> RIGHT -> ROOT", positions)

cv2.destroyAllWindows()