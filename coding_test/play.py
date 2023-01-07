a ={1,2,3}

b = {1,2,3,4}

c = b

c.update(a)
print(c == b)

print(c)
print(b)