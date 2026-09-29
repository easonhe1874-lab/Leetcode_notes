"""
LeetCode 283. 移动零 (Move Zeroes)

【题目描述】
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

【深度分析与坑点】
1. 避坑指南：严禁使用 `nums.remove(0)` 或 `nums.pop(i)`！因为这些操作每次都会触发数组元素的整体平移，导致时间复杂度恶化至 O(N^2)。
2. 核心逻辑（快慢双指针）：
   - `fast` 指针负责探索数组，寻找非零元素。
   - `slow` 指针指向当前待填充非零元素的目标位置。
   - 当 `fast` 遇到非零元素时，与 `slow` 指针位置处的元素交换，并将 `slow` 右移一位。
3. 效果：一次遍历即可把非零元素按原顺序推到数组左侧，剩下的 0 自然被挤到右侧。

【复杂度分析】
- 时间复杂度: O(N)，只对数组进行了一次单向扫描。
- 空间复杂度: O(1)，严格要求原地修改（In-Place）。
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # 交换快慢指针元素，保持相对顺序
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
