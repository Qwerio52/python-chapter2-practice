# 温度转换，eval输入，输出整数
TempStr = eval(input("请输入带符号的温度值（如：32C、80F）："))
if TempStr[-1] in ['C','c']:
    F = eval(TempStr[0:-1]) * 1.8 + 32
    print("转换后的华氏温度是{}F".format(int(F)))
elif TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print("转换后的摄氏温度是{}C".format(int(C)))
else:
    print("输入格式错误")