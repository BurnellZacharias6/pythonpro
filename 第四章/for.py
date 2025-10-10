for i in '1234567ascd':
    print(i)

for i in range(1, 5):
    print(i)

for i in range(100, 1000):
    t1 = int(str(i)[-1])
    t2 = int(str(i)[-2])
    t3 = int(str(i)[-3])
    if t1**3 + t2**3 + t3**3 == i:
        print('水仙花数:', i)

for i in range(1,20):
    if i == 7:
        break
else:
    print('循环正常结束')