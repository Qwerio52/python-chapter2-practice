# 1美元 = 6人民币，双向兑换
s = input("请输入带单位金额（如：10USD、60CNY）：")
if s[-3:] == "USD":
    num = eval(s[:-3])
    cny = num * 6
    print(f"{num}美元 = {cny}人民币")
elif s[-3:] == "CNY":
    num = eval(s[:-3])
    usd = num / 6
    print(f"{num}人民币 = {usd:.2f}美元")
else:
    print("单位错误，请用USD或CNY")