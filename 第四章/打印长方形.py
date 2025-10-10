length=eval(input("请输入打印长度："))
width=eval(input("请输入打印宽度："))
for i in range(1,width+1):
    for j in range(1,length +1):
        print("*",end="")
    print("")