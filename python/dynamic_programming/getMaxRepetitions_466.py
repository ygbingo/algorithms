"""
From leetcode 466: https://leetcode.cn/problems/count-the-repetitions/
"""

def get_max_repetitions(s1, n1, s2, n2):
    if n1 == 0: return 0
    s1cnt, index, s2cnt = 0, 0, 0
    recall = dict()
    while True:
        s1cnt += 1
        for ch in s1:
            if ch == s2[index]:
                index += 1
                if index == len(s2):
                    s2cnt, index = s2cnt + 1, 0
        if s1cnt == n1:
            return s2cnt // n2
        if index in recall:
            s1cnt_prime, s2cnt_prime = recall[index]
            pre_loop = (s1cnt_prime, s2cnt_prime)
            in_loop = (s1cnt - s1cnt_prime, s2cnt - s2cnt_prime)
            break
        else:
            recall[index] = (s1cnt, s2cnt)
    ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
    rest = (n1 - pre_loop[0]) % in_loop[0]
    for i in range(rest):
        for ch in s1:
            if ch == s2[index]:
                index += 1
                if index == len(s2):
                    ans, index = ans + 1, 0
    
    return ans // n2