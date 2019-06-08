from pythonds.basic import Stack
from pythonds.trees import BinaryTree


def buildParseTree(fpexp):
    fplist = []
    # 便览fpexp
    number = ''
    for s in fpexp:
        if s in ['+', '-', '*', '/', ')', '(']:
            if number:
                fplist.append(number)
            number = ''
            fplist.append(s)
        elif s != ' ':
            number += s

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

if __name__ == '__main__':
    pt = buildParseTree("((10+5)*3)")
    pt.postorder()  # defined and explained in the next section
