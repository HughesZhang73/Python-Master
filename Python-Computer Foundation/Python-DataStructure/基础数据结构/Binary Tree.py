# coding=utf-8


class Node(object):
    """
    定义节点类， 包含 节点元素，左孩子，右孩子节点
    """
    
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.item)


class Tree(object):
    def __init__(self):
        self.root = Node('root')  # 根节点定义为 root 永不删除，作为哨兵使用。
    
    def add(self, item):
        node = Node(item)
        if self.root is None:  # 如果二叉树为空，新插入树的点为根节点
            self.root = node
        else:
            q = [self.root]  # 如果二叉树为不为空，将 q 列表，添加二叉树的根节点
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
    
    def get_parent(self, item):
        if self.root.item == item:
            return None  # 所查询的节点 正好等于 根节点 ，说明查询的这个是根节点，根节点没有父节点
        
        temp = [self.root]
        
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left and pop_node.left.item == item:  # 某节点左子树为寻找的点
                return pop_node  # 返回某点， 即为寻找的父节点
            if pop_node.right and pop_node.right.item == item:  # 某节点的右子树为寻找的点
                return pop_node  # 返回某点，即为寻找的父节点
            
            if pop_node.left is not None:
                temp.append(pop_node.left)
            
            if pop_node.right is not None:
                temp.append(pop_node.right)
        
        return None
    
    def delete(self, item):
        if self.root is None:
            return False
        
        parent = self.get_parent(item)
        
        if parent:  # 具有子树
            
            #  左子树为空
            if parent.left.item == item:
                del_node = parent.left
            else:
                del_node = parent.right
            
            if del_node.left is None:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                
                return True
            
            # 右子树为空
            elif del_node.right is None:
                if parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
            
            #  左右子树都不为空
            else:
                tem_pre = del_node
                tem_next = del_node.right
                
                if tem_next.left is None:
                    
                    tem_pre.right = tem_next.right
                    tem_next.left = del_node.left
                    tem_next.right = del_node.right
                
                else:
                    while tem_next.left:  # 让temp指向右子树的最后一个叶子
                        tem_pre = tem_next
                        tem_next = tem_next.left
                    
                    # 替代
                    tem_pre.left = tem_next.right
                    tem_next.left = del_node.left
                    tem_next.right = del_node.right
                
                if parent.left.item == item:
                    parent.left = tem_next
                else:
                    parent.right = tem_next
                
                del del_node
                return True
        
        else:
            return False


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    
    tree.get_parent(2)