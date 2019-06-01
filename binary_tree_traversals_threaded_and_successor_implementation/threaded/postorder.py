from pythonds.trees import bst


def some_travesal(self: bst.BinarySearchTree):
    dump = bst.TreeNode(0, None)
    dump.leftChild = self.root
    self.root.parent = dump
    cur = dump
    while (cur):
        # 1. 如果当前节点的左孩子为空，则将其右孩子作为当前节点。
        if cur.leftChild == None:
            cur = cur.rightChild
        else:
            # 2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
            prevNode = cur.leftChild
            while prevNode.rightChild and prevNode.rightChild != cur:
                prevNode = prevNode.rightChild

            # a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
            if prevNode.rightChild == None:
                prevNode.rightChild = cur
                cur = cur.leftChild
            # b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空。倒序输出从当前节点的左孩子到该前驱节点这条路径上的所有节点。当前节点更新为当前节点的右孩子。
            elif prevNode.rightChild == cur:
                prevNode.rightChild = None
                print_node = prevNode
                while True:
                    print(print_node.key)
                    if print_node == cur.leftChild:
                        break
                    print_node = print_node.parent
                cur = cur.rightChild


bst.BinarySearchTree.postorder_threaded = some_travesal
if __name__ == '__main__':
    bt = bst.BinarySearchTree()
    # bt.put('c', 3)
    # bt.put('e', 5)
    # bt.put('a', 1)
    # bt.put('b', 2)
    # bt.put('d', 4)
    # bt.inorder()
    bt.put(45, None)
    bt.put(87, None)
    bt.put(23, None)
    bt.put(20, None)
    bt.put(8, None)
    bt.put(12, None)
    bt.put(2, None)
    bt.put(45, None)
    bt.put(5, None)
    bt.put(25, None)
    bt.postorder()
    print()
    bt.postorder_threaded()
