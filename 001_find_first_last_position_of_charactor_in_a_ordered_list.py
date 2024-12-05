def find(nums, target):
    return find_first_last_position(0, len(nums), nums, target)


def find_first_last_position(start, end, nums, target):
    # 终止条件1: nums为空
    if start == end:
        return [-1, -1]
    mid = start + int((end - start) / 2)
    if nums[mid] == target:
        # 以mid为基准前后遍历, 找出第一和最后一个pos
        end = mid
        # 正向向后遍历
        for index, num in enumerate(nums[mid + 1 :]):
            if num == target:
                end = mid + index + 1
            else:
                break
        # 反向向前遍历
        for index in range(mid):
            start = mid - index
            if nums[start - 1] != target:
                break
        return [start, end]
    elif nums[mid] > target:
        return find_first_last_position(start, mid, nums, target)
    else:
        return find_first_last_position(mid + 1, end, nums, target)


if __name__ == "__main__":
    nums = [5, 7, 8, 8, 8, 8, 10]
    target = 8
    print(find(nums, target))
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(find(nums, target))
    nums = []
    target = 0
    print(find(nums, target))
# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]

# 递归需要记录start/end index
# 遍历也需要
