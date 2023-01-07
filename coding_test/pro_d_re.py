
t_num = int(input())
answer = []
for i in range(t_num):
    a = input().split()[1:]
    b = input().split()[1:]

    lcs = []
    for i in range(len(b)+1):
        put = []
        for j in range(len(a)+1):
            put.append(0)
        lcs.append(put)

    for i in range(1,len(b)+1) :
        for j in range(1,len(a)+1) :
            if b[i-1] == a[j-1] :
                lcs[i][j] = lcs[i-1][j-1] + 1
            else :
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

    answer.append(lcs[-1][-1])

for i in answer:
    print(i)



