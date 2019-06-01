from pythonds.trees import bst


def inorder(self: bst.BinarySearchTree):
    cur = self.root
    while (cur):
        # 1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
        if cur.leftChild == None:
            print(cur.key)
            cur = cur.rightChild
        else:
            # 2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。

            # b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。输出当前节点。当前节点更新为当前节点的右孩子。
            try:
                if cur.prevNode and cur.prevNode.rightChild == cur:
                    cur.prevNode.rightChild = None
                    del cur.prevNode
                    print(cur.key)
                    cur = cur.rightChild
            # a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。#
            except:
                cur.prevNode = cur.leftChild
                while cur.prevNode.rightChild:
                    cur.prevNode = cur.prevNode.rightChild
                cur.prevNode.rightChild = cur
                cur = cur.leftChild


bst.BinarySearchTree.inorder_non_recursive = inorder
if __name__ == '__main__':
    bt = bst.BinarySearchTree()
    # bt.put('c', 3)
    # bt.put('e', 5)
    # bt.put('a', 1)
    # bt.put('b', 2)
    # bt.put('d', 4)
    # bt.inorder()
    bt.put(4, None)
    bt.put(3, None)
    bt.put(8, None)
    bt.put(23, None)
    bt.put(7, None)
    bt.put(9, None)
    bt.put(1, None)
    bt.put(34, None)
    bt.put(19, None)
    bt.inorder()
    print()
    bt.inorder_non_recursive()
