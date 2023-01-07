

a = 5

b = 3

fora inzzzzz
l_in = list(map(int, input().split()))

total = []
cnt = 1
for i in l_in:
    tf = 0
    for t in total:
        if i in t:
            total.remove(t)
            t.update(l_in)
            total.append(t)
            tf = 1
            break
    if tf == 0 and cnt == 1: 
        total.append(set(l_in))
        
    cnt += 1

print(total)