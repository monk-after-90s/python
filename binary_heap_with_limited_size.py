from pythonds.trees import binheap


def insert(self: binheap.BinHeap, k):
    self.heapList.append(k)
    self.currentSize = self.currentSize + 1
    self.percUp(self.currentSize)
    if self.currentSize > 10:
        self.heapList.pop()
        self.currentSize -= 1


binheap.BinHeap.insert = insert
