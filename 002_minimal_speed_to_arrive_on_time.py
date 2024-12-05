from typing import List
import math


def min_speed(dist: List[int], hour: float) -> int:
    # 边界情况
    if hour < len(dist) - 1:
        return -1
    for speed in range(max(dist), -1, -1):
        # 边界情况
        if speed == 0:
            return 1
        timeUsed = 0
        # 到站发车时间
        # 路程时间
        for index, item in enumerate(dist):
            if timeUsed >= hour:
                return speed + 1
            if index < len(dist) - 1:
                currentTime = math.ceil(item / speed)
            else:
                currentTime = item / speed
            timeUsed += currentTime
            # print(speed, timeUsed, item)
        # 最后一站到站时间
        if timeUsed > hour:
            return speed + 1


if __name__ == "__main__":
    dist = [1, 3, 2]
    hour = 6
    print(dist, hour, min_speed(dist, hour))
    dist = [1, 3, 2]
    hour = 2.7
    print(dist, hour, min_speed(dist, hour))
    dist = [1, 3, 2]
    hour = 1.9
    print(dist, hour, min_speed(dist, hour))
    dist = [1, 3, 2]
    hour = 4.1
    print(dist, hour, min_speed(dist, hour))
    dist = [1, 3, 2, 4]  # 3, 0发车, 1发车, 2发车, 3发车，4.33到/迟到
    hour = 4.1
    print(dist, hour, min_speed(dist, hour))
# 输入：dist = [1,3,2], hour = 6
# 输出：1

# 输入：dist = [1,3,2], hour = 2.7
# 输出：3

# 输入：dist = [1,3,2], hour = 1.9
# 输出：-1
