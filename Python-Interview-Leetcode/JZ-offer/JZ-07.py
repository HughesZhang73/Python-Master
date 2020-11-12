# coding=utf-8

from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.dic, self.po = {}, preorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right: return # 终止条件：中序遍历为空
        root = TreeNode(self.po[pre_root]) # 建立当前子树的根节点
        i = self.dic[self.po[pre_root]]    # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树完成划分。
        root.left = self.recur(pre_root + 1, in_left, i - 1) # 开启左子树的下层递归
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right) # 开启右子树的下层递归
        return root # 返回根节点，作为上层递归的左（右）子节点

class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder.pop(0))
        #利用python数组的index函数来定位根节点在inorder数组中的位置。
        index = inorder.index(root.val)
        # preorder数组不需要进行切片操作，递归终止条件主要靠代码前两行中的not inorder来终止。
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        return root


class Solution3:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        inord_valindex = {val: index for index, val in enumerate(inorder)}
        
        def treeBuild(prestart, preend, inordstart, inorderend):
            if prestart > preend and inordstart > inorderend:
                return None
            
            rootval = preorder[prestart]
            index = inord_valindex[rootval]
            root = TreeNode(rootval)
            root.left = treeBuild(prestart + 1, prestart + 1 + index - inordstart - 1, inordstart, index - 1)
            root.right = treeBuild(prestart + 1 + index - inordstart, preend, index + 1, inorderend)
            return root
        
        return treeBuild(0, len(preorder) - 1, 0, len(inorder) - 1)
