import random

def randomN(n):
	listR=[]
	if n > 100:
		print("Over Range")
		return None
	for i in range(1,n+1):				#循环
		R = random.uniform(1,1000)		#生成随机数
		R = int(R)						#取整
		#R = round(R)					#另一种取整
		
		listR.append(R)					#将随机数加入listR中
	
	return Single(listR)			#去重
	
	#return set(listR)		python内置的去重函数
	
#直接暴力去重，不想管了。。。。。╰(￣▽￣)╮
def Single(listR):	
	list1=[]
	
	for i in listR:
		if not (i in list1):
			list1.append(i)
			
	return len(list1),mergeSort(list1)		#传进归并排序

def mergeSort(data):
	if len(data) <= 1:
		return data
		
	mid = len(data) // 2
	
	left = mergeSort(data[:mid])
	right = mergeSort(data[mid:])
	
	return merge(left,right)
	
def merge(left,right):
	result = []
	i = 0
	j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	
	result = result + left[i:] + right[j:]		#加入剩余元素
	
	return result
	
	
	
	
	



