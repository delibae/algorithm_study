test_num = int(input())
answer = []
for ti in range(test_num):
    l_num = list(map(int, input().split()))
    total = []
    for bi in range(l_num[1]):
        l_in = list(map(int, input().split()))
        tf = 0
        for t in total:
            if ((l_in[0] in t) or (l_in[1] in t)):
                total.remove(t)
                t.update(l_in)
                total.append(t)
                tf = 1
    
        if tf == 0:
            total.append(set(l_in))
    # print("totalb", total)
    while(1):
        tf = 0
        totalv = total
        for t in totalv:
            for item in t:
                for tt in totalv:
                    if((item in tt) and (t != tt)):

                        total.remove(t)
                        total.remove(tt)
                        tt.update(t)
                        total.append(tt)
                        tf = 1
                        break
                if tf ==1:
                    break
        if (tf ==0):
            break
    # print("totala", total)
    max = -99
    for i in total:
        if len(i) > max:
            max = len(i)
    answer.append(max)



for i in answer:
    print(i)

