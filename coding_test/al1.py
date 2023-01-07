from sys import stdin
import heapq
t_num = int(stdin.readline())
total_ans = []

for tn in range(t_num):
  INF = 99
  graph = []

  n = int(stdin.readline())

  graph = [[INF] * n for _ in range(n)]
      
  for i in range(n):
      con = list(map(int,stdin.readline().split()))[1:]
      for j in con:
          graph[i][j-1] = 1
  for i in graph:
    # print(i)
    pass

  for k in range(n):
      graph[k][k] = 0
      for i in range(n):
          for j in range(n):
              graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


  for row in graph:
      for i in range(n):
          if row[i] == INF:
              row[i] = 0
      

  start, end = map(int, stdin.readline().split())
  # print(graph[start-1][end-1])
  total_ans.append(graph[start-1][end-1])

for i in total_ans:
  if i == 0:
    print("No")
  else:
    print(i)
    