'''
Leetcode 242. 有效字母异位词
题目概览:给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的
难度：简单
分类：哈希表/数组计数/字符串

解题思路：
1.首先判断两个字符串的长度是否相等，如果不相等，直接返回 False。
2.首先创建一个空列表recode，长度为26
3.遍历字符串s，并将其转化为ASCII码，减去字符串'a'的ASCII码，得到对应的索引位置，然后将recode中对应位置的值加1。
例如s[1] = 'a' 时， ord(s[1]) - ord('a') = 0, 此时对应的索引位置为0，将recode[0]加1，也就是a的计数加1。
4.遍历字符串t，并将其转化为ASCII码，减去字符串'a'的ASCII码，得到对应的索引位置，然后将recode中对应位置的值减1。
5.最后遍历recode列表，如果所有元素都为0，则说明t是s的字母异位词，返回True；否则返回False。

复杂度分析：
- 时间复杂度：O(n)，其中 n 是字符串的长度。我们需要遍历两个字符串各一次。
- 空间复杂度：O(1)，因为我们使用了一个固定大小的列表，为26个小写英文字母。
'''

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    record = [0] * 26
    for i in s:
        record[ord(i) - ord('a')] += 1
    for i in t:
        record[ord(i) - ord('a')] -= 1
    for count in record:
        if count != 0:
            return False
    return True