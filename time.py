# def time():
	# while True:
		# timein = input("请输入正整数")
		# if(round(float(timein)) >= 0 and "." not in timein):
			# break
		# print("请输入正整数")
	# print(str(timein)+"秒等价于"+str(divmod(int(timein),60)[0])+"分"+str(divmod(int(timein),60)[1])+"秒")
	
	

	
def time():
	while True:															#进行判断
		timein = input("请输入正整数")	
		if(round(float(timein)) >= 0 and "." not in timein):			#如果满足条件则跳出循环
			timeout = str(timein)										#转换输出
			minutes = int(timein) // 60									#取分
			second = int(timein) % 60									#取秒
			break
		print("请输入正整数")											#提示用户
	print(str(timeout)+"秒等价于"+str(minutes)+"分"+str(second)+"秒")	#最后输出
	