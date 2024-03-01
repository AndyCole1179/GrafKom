tuple_1 = (
    (400,400),
    (300,300),
    (100,300),
    (200,300),
    (300,400)
)
tuple_2 = (
    (400,400),
    (300,300),
    (100,300),
    (200,300),
    (300,400)
)
temp = ()
temp1 = ()
for i in range(len(tuple_1)):
    dif = int(tuple_1[i][0])+3 
    temp += (tuple_1[i][0]+3,tuple_1[i][1]+4),
    temp1 += tuple_2[i][0]+9,tuple_2[i][1]+9,
    print(tuple_1[i][0],tuple_2[i])
print(temp)
print(temp1)
y = 77
p = 0.77
z = p+y
print(z)