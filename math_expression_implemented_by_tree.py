from pythonds.basic import Stack
from pythonds.trees import BinaryTree


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree


def printexp(tree):
    sVal = ""
    if tree:
        leftchild = tree.getLeftChild()
        sVal = ('(' if leftchild else '') + printexp(leftchild)
        sVal = sVal + str(tree.getRootVal())
        rightchild = tree.getRightChild()
        sVal = sVal + printexp(rightchild) + (')' if rightchild else '')
    return sVal


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(printexp(pt))

# pt.postorder()  # defined and explained in the next section
