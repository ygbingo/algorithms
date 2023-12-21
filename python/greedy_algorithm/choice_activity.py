"""
活动选择问题：
给出一个活动列表包含开始和结束时间，求相互兼容的活动的最大数量
"""


def choice_activity(activities) -> int:
    sorted(activities, key=lambda activity: activity[1])  # 根据活动的结束时间排序
    n = len(activities)
    choice_lst = [activities[0]]  # 最先结束的活动一定在结果集里
    k = 0  # 代表上一次选择的活动
    for m in range(1, n):
        if activities[m][0] >= activities[k][1]:
            choice_lst.append(activities[m])
            k = m
    print(choice_lst)
    return len(choice_lst)

