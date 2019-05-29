from pythonds.basic import Stack
from pythonds.trees import BinaryTree


def buildParseTree(fpexp):
    fplist = fpexp.split()

    pStack = Stack()
    eTree = BinaryTree('')
    # pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i in ['and', 'or']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == 'not':
            currentTree = pStack.pop()
            currentTree.setRootVal(i)
            # currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i == ')':
            if pStack.size() > 0 and pStack.peek():
                currentTree = pStack.pop()
        elif i in ['False', 'True']:
            try:
                currentTree.setRootVal(True if i == 'True' else False)
                parent = pStack.pop()
                currentTree = parent
            except ValueError:
                raise ValueError('{}is not a boolen value'.format(i))
    return eTree


def evaluate(parseTree):
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    # 二元操作符
    if leftC and rightC:
        if parseTree.key == 'and':
            return evaluate(leftC) and evaluate(rightC)
        elif parseTree.key == 'or':
            return evaluate(leftC) or evaluate(rightC)
    # 一元操作符
    elif leftC and not rightC and parseTree.key == 'not':
        return not evaluate(leftC)
    elif not leftC and not rightC:
        return True if parseTree.getRootVal() == 'True' else False


if __name__ == '__main__':
    pt = buildParseTree('( ( not ( True and False ) ) and ( ( False or False ) and True ) )')
    pt.postorder()
    print("\n", evaluate(pt))
