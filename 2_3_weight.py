# 千克 ↔ 磅 双向转换
s = input("请输入带单位重量（如：10kg、20lb）：")
if s[-2:] == "kg":
    num = eval(s[:-2])
    lb = num * 2.2046
    print(f"{num}千克 = {lb:.2f}磅")
elif s[-2:] == "lb":
    num = eval(s[:-2])
    kg = num / 2.2046
    print(f"{num}磅 = {kg:.2f}千克")
else:
    print("单位错误，请用kg或lb")