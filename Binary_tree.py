class newNode:
    def __init__(self,key):
        self.val=key
        self.right=None
        self.left=None
def fullnode(root):
    if root!=None:
        fullnode(root.left)
        if(root.left!=None)and(root.right!=None):
            print(root.val,end=' ')
        fullnode(root.right)
def inorder(root):
    if(root==None):
        return;
    inorder(root.left)
    print(root.val)
    inorder(root.right)
def printOddNodes(root, isOdd = True): 
      
    # If empty tree  
    if (root == None):  
        return
  
    # If current node is of odd level  
    if (isOdd):  
        print(root.val, end = " ") 
  
    # Recur for children with isOdd  
    # switched.  
    printOddNodes(root.left, not isOdd)  
    printOddNodes(root.right, not isOdd) 
"""function to insert element in binary tree """
def insert(temp,key): 
  
    q = []  
    q.append(temp)  
  
    # Do level order traversal until we find  
    # an empty place.  
    while (len(q)):  
        temp = q[0]  
        q.pop(0)  
  
        if (not temp.left): 
            temp.left = newNode(key)  
            break
        else: 
            q.append(temp.left)  
  
        if (not temp.right): 
            temp.right = newNode(key)  
            break
        else: 
            q.append(temp.right)  
root = newNode(1)  
root.left = newNode(2)  
root.right = newNode(3)  
root.left.left = newNode(4)  
root.right.left = newNode(5)  
root.right.right = newNode(6)  
root.right.left.right = newNode(7)  
root.right.right.right = newNode(8)  
root.right.left.right.left = newNode(9)  
fullnode(root)
inorder(root)
printOddNodes(root)
key=12
insert(root,key)
    
        
