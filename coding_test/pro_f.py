total_ans = []
t_num = int(input())
for tn in range(t_num):
    
    
    graph = []

    num = int(input())

    for i in range(num):
        put = []
        for j in range(num):
            put.append(0)
        graph.append(put)
        
    for i in range(num):
        con = list(map(int,input().split()))[1:]
        for j in con:
            graph[i][j-1] = 1

    st = list(map(int, input().split()))

    start = st[0] -1

    end = st[1] - 1

    for i in graph:
        print(i)
    path = []

    path_all = []
    def find_path(path):
        s = path[-1]
        tf = 0
        for i in range(num):
            if i != s:
                if graph[s][i] == 1 and i == end:
                    path.append(i)
                    print("최종", path)
                    path_all.append(path)
                    tf = 1
                    return
                elif graph[s][i] == 1:
                    path.append(i)
                    tf = 1
                    find_path(path)
        return
                    
    path.append(start)
    find_path(path)
    print(path_all)
    mm = 9999
    for i in path_all:
        if len(i) < mm:
            mm = len(i)

    if  len(path_all) == 0:
        total_ans.append("No")
    else:
        total_ans.append(mm-1)
        
for i in total_ans:
    print(i)