'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

链接：https://leetcode-cn.com/problems/merge-intervals
'''
class Solution:
    def merge(self, intervals: list) -> list:
        '''
        解法1：按首位排序，构造新列表
        '''
        intervals.sort(key=lambda x:x[0])
        res = []
        for itv in intervals:       # 挨个扫描
            if not res or res[-1][1] < itv[0]:  # 对比边界大小
                res.append(itv)
            else:
                res[-1][1] = max(itv[1], res[-1][1])
        return res


if __name__ == "__main__":
    print(Solution().merge([[1,4],[4,5]]))