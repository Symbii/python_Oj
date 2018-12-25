class treenode:
    def __init__(self, val):
        self.left  = None
        self.right = None
        self.value = val

def mergeTwoBinTree(t1,t2):
    if t1==None and t2==None:
        return None
    elif t1 != None and t2 != None:
        newnode = treenode(t1.value+t2.value)
        newnode.left = mergeTwoBinTree(t1.left, t2.left)
        newnode.right = mergeTwoBinTree(t1.right, t2.right)
    elif t1 == None and t2 != None:
        newnode = treenode(t2.value)
        newnode.left = mergeTwoBinTree(None, t2.left)
        newnode.right = mergeTwoBinTree(None, t2.right)
    elif t1 != None and t2 == None:
        newnode = treenode(t2.value)
        newnode.left = mergeTwoBinTree(t1.left, None)
        newnode.right = mergeTwoBinTree(t1.left, None)
    return newnode