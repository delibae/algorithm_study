

def an(n):
    answer = []
    shape = [[],[],[]]
    for i in range(n):
        shape[0].append(n-i)
    def han(n, s, e, sp):
    
        if n == 1: 
            move = shape[s-1].pop(-1)
            shape[e-1].append(move)
            answer.append([move,s, e])
            return
        han(n-1, s, sp, e) 
        move = shape[s-1].pop(-1)
        shape[e-1].append(move)
        answer.append([move,s, e])
        han(n-1, sp, e, s) 
    han(n,1,3,2)
    return answer

nn = int(input())

for n in range(nn):
    n = n+1
    answer = an(n)
    print(n)
    for i in answer:
        print(i[0], i[1], i[2])