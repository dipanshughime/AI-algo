def dls(graph, node, goal, depth_limit):
    if node == goal:
        return [node]


    if depth_limit == 0:
        return None


    for neighbor in graph[node]:
        print(neighbor)


        result = dls(graph, neighbor, goal, depth_limit - 1)
        if result is not None:
            return [node] + result


    return None


def iterative_deepening_dfs(graph, start, goal, depth_limit):
    for limit in range(depth_limit + 1):
        result = dls(graph, start, goal, limit)
        if result is not None:
            return result
    return None

graph = {
    '1': ['2', '7', '8'],
    '2': ['3', '6'],
    '3': ['4', '5'],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': ['9','12'],
    '9': ['10','11'],
    '10': [],
    '11': [],
    '12': []
}


start_node='1'
goal_node='11'
depth=3


result = iterative_deepening_dfs(graph, start_node, goal_node, depth)


if result:
    print("Path found:", result)
else:
    print("Path not found within depth limit.")
