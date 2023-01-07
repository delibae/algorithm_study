import heapq

def dijkstra(graph, start):
  dis = {node: 99 for node in graph}  
  dis[start] = 0 
  queue = []
  heapq.heappush(queue, [dis[start], start]) 

  while queue:
    current, current_des = heapq.heappop(queue) 

    if dis[current_des] < current:
      continue
    
    for new_des, new_dis in graph[current_des].items():
      distance = current + new_dis
      if distance < dis[new_des]:
        dis[new_des] = distance
        heapq.heappush(queue, [distance, new_des])
    
  return dis

def make_graph():
    n = int(input())
    graph = {}
    for i in range(n):
        put = list(map(int,input().split()))
        if len(put) != 1:
            pput = {}
            for j in put[1:]:
                pput[j] = 1
            graph[put[0]] = pput
        else:
            graph[put[0]] = {}
    return graph


total_ans = []

t_num = int(input())
for tn in range(t_num):
    graph = make_graph()
    s,e = map(int,input().split())
    
    result = dijkstra(graph, s)

    r = result[e]

    if (r == 0 or r == 99):
        final = 'No'
    else:
        final = r   
        
    total_ans.append(final)

for i in total_ans:
    print(i)
    