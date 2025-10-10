import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

luck_num=7
my_name='小明'
print('luck_num的类型是',type(luck_num))
print('my_name的类型是',type(my_name))

print(my_name,'的幸运数字是',luck_num)
luck_num='sss'
print('luck_num的类型是',type(luck_num))

no=num=1024
print('no的值是',no)
print('num的值是',num)
print(id(no),id(num))