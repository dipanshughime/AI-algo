import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth, path=[]):
    if curDepth == targetDepth:
        return scores[nodeIndex], path + [nodeIndex]
    
    multiplier = 1 if maxTurn else -1
    leftScore, leftPath = minimax(curDepth + 1, nodeIndex * 2, not maxTurn, scores, targetDepth, path + [nodeIndex])
    rightScore, rightPath = minimax(curDepth + 1, nodeIndex * 2 + 1, not maxTurn, scores, targetDepth, path + [nodeIndex])

    return (leftScore, leftPath) if multiplier * leftScore > multiplier * rightScore else (rightScore, rightPath)

scores = [int(score) for score in input("Enter scores (space-separated): ").split()]

treeDepth = int(math.log(len(scores), 2))
optimalValue, path = minimax(0, 0, True, scores, treeDepth)

print("The value selected is:", optimalValue)
print("Path:")
for i, node in enumerate(path):
    print(f"Level {i}: Node {node}")
print("Path is:", path)
