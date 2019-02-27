"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
def postorder(root: 'Node'):
    ret = list()
    if root is None:
        return ret
    elif root.children is not None:
        for ch in root.children:
            ret.extend(postorder(ch))

    ret.append(root.val)
    return  ret