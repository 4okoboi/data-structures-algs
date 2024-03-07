from typing import List


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


class Tree:
    def __init__(self, root_value):
        self.root = Node(value=root_value)

    def add_element(self, value: int):
        last_node = self.root
        while True:
            if value < last_node.value:
                if last_node.left:
                    last_node = last_node.left
                else:
                    last_node.left = Node(value=value)
                    return
            elif value > last_node.value:
                if last_node.right:
                    last_node = last_node.right
                else:
                    last_node.right = Node(value=value)
                    return

    def find(self, val: int) -> Node or None:
        now_node = self.root
        if val == now_node.value:
            return now_node
        while True:
            if now_node.value < val:
                if now_node.right is None:
                    return None
                elif now_node.right.value == val:
                    return now_node.right
                else:
                    now_node = now_node.right
            else:
                if now_node.left is None:
                    return None
                elif now_node.left.value == val:
                    return now_node.left
                else:
                    now_node = now_node.left
                    
    def dfs(self) -> List:
        if self.root is None:
            return []

        stack = [self.root]
        result = []

        while stack:
            now_node = stack.pop()
            result.append(now_node.value)
            
            if now_node.right:
                stack.append(now_node.right)
            if now_node.left:
                stack.append(now_node.left)

        return result
    
    def bfs(self) -> List:
        if self.root is None:
            return []

        queue = [self.root]
        result = []
        
        while queue:
            now_node = queue.pop(0)
            result.append(now_node.value)
            
            if now_node.left:
                queue.append(now_node.left)
            if now_node.right:
                queue.append(now_node.right)
        
        return result
            


tree = Tree(4)

tree.add_element(2)
tree.add_element(7)
tree.add_element(1)
tree.add_element(3)

print(tree.bfs())

