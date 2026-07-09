class Solution:
    def validTree(
        self,
        number_of_nodes: int,
        edges: List[List[int]]
    ) -> bool:
        """
        A graph is a valid tree if:

        1. It contains NO cycle.
        2. Every node is connected.
        """

        # Empty graph is considered a tree.
        if number_of_nodes == 0:
            return True

        # ---------------------------------
        # Build adjacency list
        #
        # Since the graph is undirected,
        # add edges in both directions.
        # ---------------------------------
        adjacency_list = {
            node: []
            for node in range(number_of_nodes)
        }

        for node_a, node_b in edges:
            adjacency_list[node_a].append(node_b)
            adjacency_list[node_b].append(node_a)

        # Stores nodes already visited
        visited = set()

        def dfs(current_node, parent_node):
            """
            Returns False if a cycle is found.
            Otherwise returns True.
            """

            # Visiting the same node again
            # means we've found a cycle.
            if current_node in visited:
                return False

            visited.add(current_node)

            # Explore all neighbours
            for neighbour in adjacency_list[current_node]:

                # Ignore the edge
                # that brought us here.
                if neighbour == parent_node:
                    continue

                if not dfs(neighbour, current_node):
                    return False

            return True

        # Tree must satisfy BOTH:
        #
        # 1. No cycle
        # 2. Every node visited
        return (
            dfs(0, -1)
            and
            len(visited) == number_of_nodes
        )