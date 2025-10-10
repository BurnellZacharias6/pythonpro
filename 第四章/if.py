num = eval(input("请输入中奖号码:"))
if num == 123456:
    print("恭喜你中奖了！")
else:
    print("很遗憾，您没有中奖。")

print('----------')
s=eval(input("请输入检测数据："))
if s%2:
    print("奇数")

if not s%2:
    print("偶数")

print('未中奖' if num != 123456 else '中奖')

x=eval(input("请输入一个数字："))
if x==1:
    print('一')
elif x==2:
    print('二')
elif x==3:
    print('三')
elif x==4:
    print('四')
else: print('其他数字')