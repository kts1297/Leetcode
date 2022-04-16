# https://leetcode.com/problems/trim-a-binary-search-tree/


def trimBST(root, low, high):
    if root is None:
        return root
    if root.val < low:
        return trimBST(root.right, low, high)
    elif root.val > high:
        return trimBST(root.left, low, high)
    else:
        root.left = trimBST(root.left, low, high)
        root.right = trimBST(root.right, low, high)
        return root
