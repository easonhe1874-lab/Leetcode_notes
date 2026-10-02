"""
LeetCode 389. 找不同 (Find the Difference)

【题目描述】
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字符。请找出在 t 中被添加的字符。

【深度分析与巧妙解法】
1. 普通解法：哈希表计数，统计 s 和 t 中每个字符出现的次数，找到频次不一致的字符。
2. 极客解法（位运算异或 XOR）：
   - 异或性质：$x \oplus x = 0$ 且 $x \oplus 0 = x$。
   - 将 `s` 和 `t` 中所有字符的 ASCII 码依次连着进行异或。成对出现的字符（即 `s` 和 `t` 中原有的重复字符）全部互相抵消为 0，最后剩下的值转换为字符即为多出来的那个字符！

【复杂度分析】
- 时间复杂度: O(N)，只需对 s 和 t 的字符进行一次扫描。
- 空间复杂度: O(1)，仅使用一个整型变量维护累加结果。
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        # 依次异或 s 和 t 中所有字符的 ASCII 码
        for ch in s:
            res ^= ord(ch)
        for ch in t:
            res ^= ord(ch)
            
        return chr(res)
