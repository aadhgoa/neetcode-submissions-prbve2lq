from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):

        INFINITY = float('inf')

        edges = defaultdict(list)

        # Build graph
        for u, v, t in times:
            edges[u].append((v, t))

        # Distance array
        dist = {
            node: INFINITY
            for node in range(1, n + 1)
        }

        dist[k] = 0

        visited = set()

        # Dijkstra
        for _ in range(n):

            min_node = None
            min_distance = INFINITY

            # Find minimum unvisited node
            for node in range(1, n + 1):

                if node not in visited and dist[node] < min_distance:

                    min_distance = dist[node]
                    min_node = node

            # No reachable nodes left
            if min_node is None:
                break

            visited.add(min_node)

            # Relax neighbors
            for neighbour, time in edges[min_node]:

                new_distance = time + dist[min_node]

                # IMPORTANT FIX
                if new_distance < dist[neighbour]:

                    dist[neighbour] = new_distance

        max_distance = max(dist.values())

        # Some node unreachable
        if max_distance == INFINITY:
            return -1

        return max_distance