



a = [0, 1, 0, 0, 0, 0]
b = [1, 0, 1, 0, 0, 0]
c = [0, 1, 0, 1, 0, 0]
d = [0, 0, 1, 0, 1, 0]
e = [0, 0, 0, 1, 0, 1]
f = [0, 0, 0, 0, 1, 0]
graph = [a,b,c,d,e,f]

for i in graph:
    print(i)
    
start = 0

end = 1

num = 6
def find_path(path):
    s = path[-1]
    tf = 0
    for i in range(num):
        if i != s:
            if graph[s][i] == 1 and i == end:
                path.append(i)
                print("최종", path)
                tf = 1
                return
            elif graph[s][i] == 1:
                path.append(i)
                tf = 1
                find_path(path)
    return

find_path([start])