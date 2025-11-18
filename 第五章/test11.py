list={88,89,90,98,00,99}
result=[]
for item in list:
    if item == 0:
        result.append(str(200)+str(item))
    else:
        result.append(str(19)+str(item))
print(result)