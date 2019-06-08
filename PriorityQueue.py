from pythonds.trees import BinHeap


class PriorityQueue:
    def __init__(self, alist=None):
        self.binheap = BinHeap()
        if alist:
            self.binheap.buildHeap(alist)

    def enqueue(self, new_item):
        self.binheap.insert(new_item)

    def dequeue(self, aitem):
        try:
            index = self.binheap.heapList.index(aitem)
            if 0 < index <= self.binheap.currentSize:
                self.binheap.heapList[index], self.binheap.heapList[self.binheap.currentSize] = self.binheap.heapList[
                                                                                                    self.binheap.currentSize], \
                                                                                                self.binheap.heapList[
                                                                                                    index]
                self.binheap.heapList.pop()
                self.binheap.currentSize -= 1
        except ValueError:
            print("不存在")


if __name__ == '__main__':
    pq = PriorityQueue([4, 3, 8, 1, 5, 9, 2])
    # pq.enqueue(1.5)
    pq.dequeue(10)
