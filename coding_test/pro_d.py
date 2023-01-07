a = ["99999", "00001", "01234", "12345", "77777", "44444", "98765"]

b = ["01234" ,"12345" ,"99999" ,"44444" ,"98765"]

b = ["99999" ,"44444" ,"98765"]

same = list(set(a) & set(b))

for i in a:
    if i not in same:
        a.remove(i)

for i in b:
    if i not in same:
        b.remove(i)
        
print(a)
print(b)
# answer_all = []
# answer = []
# for start in range(len(a)):
#     print("-------------------")
#     a_in = a.index(a[start])
#     b_in = b.index(a[start])

#     a_v = a[a_in:]
#     b_v = b[b_in:]
#     print(a_v)
#     print(b_v)
#     for ss in range(len(a_v)-1):
#         ss = ss + 1 
#         a_in = a_v.index(a_v[ss])
#         if a_v[ss] not in b_v:
#             break
#         b_in = b_v.index(a_v[ss])
#         a_vv = a_v[a_in:]
#         b_vv = b_v[b_in:]
#         print(a_vv)
#         print(b_vv)
#         break
#     print("-------------------")


# print("--------------------------")


answer_all = []

def find_all(a,b, answer):
    answer.append(a[0])
    del a[0]
    del b[0]
    
    for start in range(0,len(a)):
        tf = 0
        print(start)
        a_in = a.index(a[start])
        if a[start] not in b:
            answer_all.append(answer)
            tf = 1
        elif len(a) == 1:
            answer.append(a[0])
            answer_all.append(answer)
            tf = 1
        else:
            answer.append(a[start])
            
        if tf == 0:
            b_in = b.index(a[start])
            a = a[a_in:]
            b = b[b_in:]
            find_all(a,b,answer)
        else:
            return
        
        
find_all(a,b,[])

print(answer_all)