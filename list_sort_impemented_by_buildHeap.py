from pythonds.trees import binheap


#
# def buildHeap(self, alist):
#     i = len(alist) // 2
#     self.currentSize = len(alist)
#     self.heapList = [0] + alist[:]
#     print(len(self.heapList), i)
#     while (i > 0):
#         print(self.heapList, i)
#         self.percDown(i)
#         i = i - 1
#     print(self.heapList, i)

def sort_list(self: binheap.BinHeap):
    newlist = [0]
    for index in range(self.currentSize, 0, -1):
        self.heapList[1], self.heapList[index] = self.heapList[index], self.heapList[1]
        newlist.append(self.heapList[index])
        self.buildHeap(self.heapList[1:index])
    self.heapList = newlist


binheap.BinHeap.sort_list = sort_list

if __name__ == '__main__':
    bh = binheap.BinHeap()
    # bh.buildHeap([35, 245, 6, 24, 78, 34, 98, 45, 5, 987, 34, 7])
    # bh.sort_list()
    # print(bh.heapList[1:])



