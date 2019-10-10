'''
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

链接：https://leetcode-cn.com/problems/path-sum-iii
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        '''
        解法1：递归，nums存储所有上级节点的可能的路径和，当递归到一个新的节点时，
        根据nums生成一个新列表包含所有上级节点到当前节点的路径和，将新生成的列表传递给子节点进行递归
        '''
        # def dfs(node: TreeNode, nums: list):
        #     parent_sum = [num + node.val for num in nums] + [node.val]
        #     return parent_sum.count(sum) + (dfs(node.left, parent_sum) if node.left else 0) + (dfs(node.right, parent_sum) if node.right else 0)
        # return dfs(root, []) if root else 0
        '''
        解法2：递归，以每个节点为根节点递归计算一遍路径和为sum的数量，多次递归，重复计算太多，效率低
        '''
        def dfs(node: TreeNode, target: int) -> int:
            return (1 if node.val == target else 0) + \
                (dfs(node.left, target-node.val) if node.left else 0) + \
                (dfs(node.right, target-node.val) if node.right else 0)
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum) if root else 0
