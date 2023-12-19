"""
Leetcode32: 最长有效括号, 给你一个只包含 '(' 和 ')' 的字符串，
找出最长有效（格式正确且连续）括号子串的长度。
"""
def longest_valid_parentheses(s: str) -> int:
    if not s: return 0
    res = [0] * len(s)
    for i in range(1, len(s)):
        j = i - res[i-1] - 1
        if s[i] == ")":
            if s[i-1] == "(":
                res[i] = res[i-2] + 2
            elif j >= 0 and s[j] == "(":
                new_res = res[i-1] + 2
                res[i] = new_res + res[i-new_res]
    return max(res)