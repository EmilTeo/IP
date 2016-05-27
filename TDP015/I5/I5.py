def postorder(tree):
    if(isinstance(tree, tuple)):
        tL =tree[0]
        r = tree[1]
        tR =tree[2]
        return(r + postorder(tL) + postorder(tR))
    return tree
print(postorder((('1', '*', '2'), '+', (('3', '+', '4'), '*', '5'))))


def inorder(tree):
    if(isinstance(tree, tuple)):
        tL =tree[0]
        r = tree[1]
        tR =tree[2]
        return(inorder(tL) +r + inorder(tR))
    return tree
print(inorder((('1', '*', '2'), '+', (('3', '+', '4'), '*', '5'))))

def preorder(tree):
    if(isinstance(tree, tuple)):
        tL =tree[0]
        r = tree[1]
        tR =tree[2]
        return(preorder(tL) + preorder(tR) + r)
    return tree
print(preorder((('1', '*', '2'), '+', (('3', '+', '4'), '*', '5'))))
