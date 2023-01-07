#오일러트레일조건
t_num = int(input())
total_ans = []
for tn in range(t_num):
    n,m = map(int,input().split())

    l = []
    for i in range(m):
        l.append(list(map(int,input().split())))
    #condition 1
    cnt = 0
    tf = 0
    for i in range(len(l)):

        for j in range(len(l[i])):
            if l[i][j] == 0:
                cnt += 1
            c2_cnt = 0
            if i-1 > -1:
                if l[i-1][j] == 0:
                    c2_cnt += 1
            if j-1 > -1: 
                if l[i][j-1] == 0:
                    c2_cnt += 1
            if i+1 < m:
                if l[i+1][j] == 0:
                    c2_cnt += 1
            if j+1 < n:
                if l[i][j+1] == 0:
                    c2_cnt += 1

            if c2_cnt%2 != 0:
                tf += 1
            

    if cnt%2==0 or (tf==0 or tf ==2):
        total_ans.append(1)
    else:
        total_ans.append(0)

for i in total_ans:
    print(i)