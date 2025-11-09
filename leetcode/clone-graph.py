"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # O(n) time and space where n is number of nodes in graph
        def dfs(current_node):
            if current_node is None:
                return None
            
            if current_node in visited_nodes:
                return visited_nodes[current_node]
            
            cloned_node = Node(current_node.val)

            visited_nodes[current_node] = cloned_node

            for neighbor in current_node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            
            return cloned_node
        
        visited_nodes = {}

        return dfs(node)