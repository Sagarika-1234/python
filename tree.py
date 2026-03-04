def level(root):
    if not root:
        return[]
    q=[root]
    res=[]
    while q:
        node=q.pop(0)
        res.append(noode.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        return res
arr=[1,2,3,4,5,6]
btree=createbt(arr,1,len(arr))
print(level(btree))
