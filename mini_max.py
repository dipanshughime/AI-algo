import math

def fun_Minmax(cd, node, maxt, scr, td):
    if cd == td:
        return scr[node]  

    if maxt:
        return max(fun_Minmax(cd + 1, node * 2, False, scr, td), fun_Minmax(cd + 1, node * 2 + 1, False, scr, td))
    else:
        return min(fun_Minmax(cd + 1, node * 2 , True, scr, td), fun_Minmax(cd + 1, node * 2 + 1, True, scr, td))

scr = []
x = int(input('Enter the total number of leaf nodes: '))
for i in range(x):
    y = int(input('Enter the value of the leaf node: '))
    scr.append(y)

td = int(math.log(len(scr), 2))
ct = int(input('Enter the current depth: '))
maxt = True
node = int(input('Enter the starting node: '))

ans = fun_Minmax(ct, node, maxt, scr, td)
print(ans)
