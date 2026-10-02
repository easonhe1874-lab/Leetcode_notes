"""
LeetCode 242. 有效的字母异位词 (Valid Anagram)

【题目描述】
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词（字符相同但顺序不同）。

【深度分析与坑点】
1. 核心逻辑：
   - 先检查两字符串长度是否相等，不相等直接返回 False。
   - 使用长度为 26 的频次数组（相当于固定大小的 Hash 表），`s` 的字符做加法（+1），`t` 的字符做减法（-1）。
   - 若最终数组中所有元素均为 0，则说明两字符串字符频次完全一致。
2. 工程对比：相比开辟 Python `dict`，使用固定大小的固定数组（Array）在 CPU 缓存和内存占用上性能更优。

【复杂度分析】
- 时间复杂度: O(N)，遍历一次字符串。
- 空间复杂度: O(1)，固定开辟 26 个位置的常数级别空间。
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counts = [0] * 26
        for c1, c2 in zip(s, t):
            counts[ord(c1) - ord('a')] += 1
            counts[ord(c2) - ord('a')] -= 1
            
        return all(x == 0 for x in counts)
