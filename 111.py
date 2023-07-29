# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return myfun(root)


def myfun(root):
    if not root:
        return 0
    q = [root]
    height = 1
    curr_nodes = 1
    res = set()
    while q:
        if curr_nodes == 0:
            curr_nodes = len(q)
            height += 1
        node = q.pop(0)
        curr_nodes -= 1
        if not node.left and not node.right:
            res.add(height)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return min(res)
