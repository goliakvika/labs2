def get_order(dependencies):
    graph = {}
    for d in dependencies:
        child, parent = d.split()
        if parent not in graph:
            graph[parent] = []
        graph[parent].append(child)

    def dfs(node, visited, order):
        visited.add(node)
        if node in graph:
            for child in graph[node]:
                if child not in visited:
                    dfs(child, visited, order)
        order.append(node)

    visited = set()
    order = []

    for node in graph.keys():
        if node not in visited:
            dfs(node, visited, order)

    return list(reversed(order))

