def profit():
	apr = eval(input("请输入年利率"))
	moneyear = eval(input("请输入本金（元）和年份，以逗号分隔"))
	money = moneyear[0]
	year = moneyear[1]
	final = money * (1 + apr/12/100)**(year*12)
	print(round(final,2))