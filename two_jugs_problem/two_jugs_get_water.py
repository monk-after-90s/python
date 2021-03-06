# 递归解决两个不明容量水壶倒指定容量水的问题
# 水壶类
import random
from copy import deepcopy


class Jug:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.currut_water = 0

    def __str__(self):
        return self.name

    # 接水
    def receivewater(self):
        self.currut_water = self.capacity

    # 倒尽水
    def pour_water(self):
        self.currut_water = 0

    # 倒水到另一壶
    def pour_to(self, other):
        # other_space = other.capacity - other.currut_water
        other_prev_water = other.currut_water
        other.currut_water = (other.currut_water + self.currut_water) \
            if (other.currut_water + self.currut_water) < other.capacity \
            else other.capacity
        self.currut_water -= (other.currut_water - other_prev_water)


# 取水函数
def get_water(jug_A: Jug, jug_B: Jug, water_goal: int, memo: list) -> bool:  # memo用于记录试过的水量组合，序号为jug_A水量，值为jug_B水量列表
    # 还未有与当前jug_A.currut_water搭配的组合
    if not isinstance(memo[jug_A.currut_water], list):
        memo[jug_A.currut_water] = [jug_B.currut_water]
        # 两个壶都满直接失败，不需要这样的无意义尝试
        if jug_A.currut_water == jug_A.capacity and jug_B.currut_water == jug_B.capacity:
            return ''
    # 还未有当前jug_A.currut_water与jug_B.currut_water搭配的组合
    elif memo[jug_A.currut_water].count(jug_B.currut_water) <= 0:
        memo[jug_A.currut_water].append(jug_B.currut_water)
        # 两个壶都满直接失败，不需要这样的无意义尝试
        if jug_A.currut_water == jug_A.capacity and jug_B.currut_water == jug_B.capacity:
            return ''
    # 出现过这种尝试，既然程序还在运行说明这个尝试失败了
    else:
        return ''

    # base case 有个水壶有了目标水量
    if jug_A.currut_water == water_goal:
        return '得到目标水量在' + str(jug_A)
    elif jug_B.currut_water == water_goal:
        return '得到目标水量在' + str(jug_B)
    # 两个壶总共的水量是目标水量
    elif jug_A.currut_water + jug_B.currut_water == water_goal:
        return '得到目标水量在' + str(jug_A) + ' ' + str(jug_B) + "共同盛放"
    # # 两个水壶都空了。玩着玩着两个水壶都倒空了还玩个毛
    # elif jug_A.currut_water == jug_B.currut_water == 0:
    #     return False
    # 递归
    else:
        # 有几种递归情况，各包含A或者B最后盛目标水量
        # 留下之前的状态，用于递归分支更改了壶状态之后从老状态开始新的测试
        current_jug_A, current_jug_B = deepcopy(jug_A), deepcopy(jug_B)
        # 随机发生顺序
        front_after = list(range(6))
        random.Random().shuffle(front_after)
        for i in front_after:
            if i == 0:
                # 1、发生水壶间倒水
                # 可能是A向B倒水
                jug_A.pour_to(jug_B)
                nextoperation = get_water(jug_A, jug_B, water_goal, memo)
                if nextoperation != '':
                    return str(jug_A) + '向' + str(jug_B) + '倒水\n' + nextoperation
                # 恢复
                jug_A, jug_B = deepcopy(current_jug_A), deepcopy(current_jug_B)
            elif i == 1:
                # 可能是B向A倒水
                jug_B.pour_to(jug_A)
                nextoperation = get_water(jug_A, jug_B, water_goal, memo)
                if nextoperation != '':
                    return str(jug_B) + '向' + str(jug_A) + '倒水\n' + nextoperation
                # 恢复
                jug_A, jug_B = deepcopy(current_jug_A), deepcopy(current_jug_B)
            elif i == 2:

                # 可能是A接水
                jug_A.receivewater()
                nextoperation = get_water(jug_A, jug_B, water_goal, memo)
                if nextoperation != '':
                    return str(jug_A) + '接满水\n' + nextoperation
                # 恢复
                jug_A, jug_B = deepcopy(current_jug_A), deepcopy(current_jug_B)

            elif i == 3:

                # 可能是B接水
                jug_B.receivewater()
                nextoperation = get_water(jug_A, jug_B, water_goal, memo)
                if nextoperation != '':
                    return str(jug_B) + '接满水\n' + nextoperation
                # 恢复
                jug_A, jug_B = deepcopy(current_jug_A), deepcopy(current_jug_B)

            elif i == 4:

                # 可能是A倒空水
                jug_A.pour_water()
                nextoperation = get_water(jug_A, jug_B, water_goal, memo)
                if nextoperation != '':
                    return str(jug_A) + '倒空水\n' + nextoperation
                # 恢复
                jug_A, jug_B = deepcopy(current_jug_A), deepcopy(current_jug_B)

            elif i == 5:

                # 可能是B倒空水
                jug_B.pour_water()
                nextoperation = get_water(jug_A, jug_B, water_goal, memo)
                if nextoperation != '':
                    return str(jug_B) + '倒空水\n' + nextoperation
                # 恢复
                jug_A, jug_B = deepcopy(current_jug_A), deepcopy(current_jug_B)
    return ''

if __name__ == '__main__':
    big_jug = Jug('', 7)
    small_jug = Jug('', 22)
    big_jug.name = str(big_jug.capacity) + 'L壶'
    small_jug.name = str(small_jug.capacity) + 'L壶'
    # 记录曾经有过的容量组合,最大序号是big_jug.capacity。用于记录试过的容量组合，序号为big_jug容量，值为small_jug容量列表
    memory_list = [0] * (big_jug.capacity + 1)
    print(get_water(big_jug, small_jug, 23, memory_list))
