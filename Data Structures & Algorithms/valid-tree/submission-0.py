class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {
            i: [] for i in range(n)
        }

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visit = set()

        def dfs(node, prevNode):
            if node in visit:
                return False
            
            visit.add(node)

            for nextNode in adj[node]:
                if nextNode == prevNode:
                    continue
                
                if not dfs(nextNode, node):
                    return False
            
            return True 
        
        return dfs(0, -1) and n == len(visit)