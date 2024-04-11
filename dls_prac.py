def dls(graph, node, goal,depth):
    if node == goal:
        return [node]
    if depth == 0:
        return None
    
    for nig in graph[node]:
        result=dls(graph,nig,goal, depth-1)
        if result is not None:
         return [node]+result
    return None

graph={
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
goal_node='12'
depth=2

result = dls(graph,start_node, goal_node, depth)

if result:
    print("Path found:", result)

else:
   print('result not found')
