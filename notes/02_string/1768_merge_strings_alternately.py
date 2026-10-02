"""
LeetCode 1768. 交替合并字符串 (Merge Strings Alternately)

【题目描述】
给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。

【深度分析与坑点】
1. 性能陷阱：在 Python 中应避免在循环内部直接进行字符串拼接（`str += char`），因为字符串是不可变对象，频繁拼接会触发多次内存重新分配（空间开销大）。
2. 最佳实践：使用列表（List）暂存每次交替产生的字符，最后通过 `''.join(res)` 一次性转换为最终字符串。

【复杂度分析】
- 时间复杂度: O(N + M)，其中 N 和 M 分别为两字符串长度。
- 空间复杂度: O(N + M)，用于存储结果字符的列表开销。
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i, j = 0, 0
        n1, n2 = len(word1), len(word2)
        
        while i < n1 or j < n2:
            if i < n1:
                res.append(word1[i])
                i += 1
            if j < n2:
                res.append(word2[j])
                j += 1
                
        return "".join(res)
