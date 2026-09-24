"""
LeetCode 459. 重复的子字符串 (Repeated Substring Pattern)
难度: 简单
分类: 字符串 / 双倍字符串 / KMP算法

解题思路:
1. 解法一（双倍字符串巧解）：
   - 将两个 s 拼接成 (s + s)，并切头去尾：(s + s)[1:-1]。
   - 若原字符串 s 依然包含在其中，说明 s 是由重复子串构成的。
   - 时间复杂度: O(N)，空间复杂度: O(N)

2. 解法二（KMP 前缀表硬核解法）：
   - 构建 KMP 的 next 数组，获取最后一个字符的最长相等前后缀长度 L。
   - 若 L > 0 且 len(s) % (len(s) - L) == 0，则说明可由最小重复单元构成。
   - 时间复杂度: O(N)，空间复杂度: O(N)
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 解法一：Python 双倍字符串一行巧解（推荐日常刷题使用）
        return s in (s + s)[1:-1]

    def repeatedSubstringPattern_kmp(self, s: str) -> bool:
        # 解法二：KMP 算法（适合面试官禁用字符串 API 场景）
        n = len(s)
        if n <= 1:
            return False

        # 1. 构建前缀表 next 数组
        nxt = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j

        # 2. 获取最长相等前后缀长度
        longest_lps = nxt[n - 1]

        # 3. 检查整除性
        return longest_lps > 0 and n % (n - longest_lps) == 0