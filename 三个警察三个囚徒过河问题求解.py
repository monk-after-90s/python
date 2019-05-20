# --*-- coding:utf-8 --*--
'''
三个警察和三个囚徒过河问题

三个警察和三个囚徒【需要】过一条河，河边只有一条船。
1）船每次最多只能载两个人。
2）无论在河的哪边，当囚徒人数多于警察的人数时，警察会
被囚徒杀死。

用程序求解让所有人安全过河的方案。

数据结构：
用一个元组来表示两边的人员分布，例如：
('3，2，1')表示 左岸：3警察2罪犯1船，右岸可以通过左
岸用一个简单的函数推算，为了方便不直接保存右岸状态。

STEP 1：
把所有人都安全的可能状态及船的状态，保存在一个列表里

STEP 2：
对列表里这些状态进行排序，如果每一种状态可以过度到下
一个状态（满足船是来回划，每次最多乘两人的规定），如
果通过这些中间状态，可以把初始状态（3，3，1）过渡到
目标状态（0，0，0），那么就找到了问题的解。
'''

from collections import deque

'''生成(警察，囚徒，船)的状态所有组合'''
allStatus = [(p,c,b) for p in range(4) for c in range(4) for b in (0,1)]

def calcRight(left):
    '''根据左岸状态，返回右岸的状态'''
    p,c,b = left
    return 3-p,3-c, 1- b

def isSafe(status):
    '''该状态是安全的吗？'''
    if 0 < status[0] < status[1]:
        return False
    else:
        return True

def filterSafe(allStatus):
    '''过滤掉那些不安全的状态'''
    d = []
    for left in allStatus:
        right = calcRight(left)
        if isSafe(right) and isSafe(left):
            d.append(left)
    return d

statusCollection = filterSafe(allStatus)

'''状态初始化，左边岸(警察，囚徒，船)的数量为(3, 3, 1)'''
s = statusCollection
init = s.index((3, 3, 1))
s[0], s[init] = s[init], s[0]
solutions = []   #用来保存最终的解决方案

def isNext(preItem=(3, 3, 1),item=(3, 1, 0)):
    '''可以从上一个状态转变为下一个状态吗？'''
    if preItem[2] == 1:
        flag = 1
    else:
        flag = -1

    police = flag*(preItem[0] - item[0])
    craminal = flag*(preItem[1] - item[1])

    if (preItem[2]+item[2] == 1) and (police,craminal) in [(1,0),(0,1),(2,0),(0,2),(1,1)]:
        return True
    else:
        return False
def statusFormat(status):
    right = calcRight(status)
    return '左岸：{}  {}  {},  右岸：{}  {}  {}'.format(*status,*right)

def find(p):
    global s
    # 在副本中循环而不是在S中循环，因为后面的操作会破环s中元素的相互位置关系
    for item in s[p:]:
        if isNext(s[p-1], item):
            s[s.index(item)], s[p] = s[p], s[s.index(item)]  #交换位置
            if s[p] == (0,0,0): solutions.append(s[:p+1])
            find(p+1)                                       #递归调用
    else:
        return
if __name__ == '__main__':
    find(p=1)    #第一个元素为初始状态，因此从第二元素开始查找。
    print(f'共找到{len(solutions)}种解决方案。现输出其中一种解决方案：')
    print('     警 囚 船        警 囚 船')
    for status in solutions[0]: print(statusFormat(status))