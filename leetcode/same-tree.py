# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        # O(N) time where N is the number of nodes in the samllest of the two trees
        # O(N) space in worst case due to recursive call to stack in linear manner
        
        # if both tree are None, they are the same and both are empty
        if p == q:
            return True
        
        if p is None or q is None or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)