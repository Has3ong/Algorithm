class TreeNode:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

def pre(pNode, ret):
    ret.append(pNode)
    if pNode.left :
        pre(pNode.left, ret)

    if pNode.right :
        pre(pNode.right, ret)

def post(pNode,ret):
    if pNode.left:
        post(pNode.left, ret)

    if pNode.right:
        post(pNode.right, ret)
    ret.append(pNode)


def mid(pNode,ret):
    if pNode.left:
        mid(pNode.left, ret)
    ret.append(pNode)
    if pNode.right:
        mid(pNode.right, ret)

def solution():

    N = int(input())
    Node = []
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(N):
        Node.append(TreeNode(i, None, None))

    for i in range(N):
        root, left, right = map(str, input().split(' '))
        if not left == '.':
            Node[Alphabet.index(root)].left = Node[Alphabet.index(left)]
        else:
            Node[Alphabet.index(root)].left = None

        if not right == '.':
            Node[Alphabet.index(root)].right = Node[Alphabet.index(right)]
        else:
            Node[Alphabet.index(root)].right = None

    ret = []
    pre(Node[0], ret)
    res = ''
    for i in ret:
        res += Alphabet[i.name]
    print(res)

    ret = []
    mid(Node[0], ret)
    res = ''
    for i in ret:
        res += Alphabet[i.name]
    print(res)

    ret = []
    post(Node[0], ret)
    res = ''
    for i in ret:
        res += Alphabet[i.name]
    print(res)

solution()