#自己挖的坑。。。跪着也要填完，大神请轻喷
#一时兴起想写的转换简谱调的代码，可以实现任意调之间的转换，啪啪啪，如果在字典中有的话。。。字典还没填完备，暂时只有其他调的全音，还无半音
#因为字典还不完备，任意调之间的转换可能会出问题，转c调是没问题的（啪啪，打脸，@_@，原本只是想任意调转c，后来脑洞又开，写任意调了）
#命令行版本。。。command line version。。。。我觉得还是函数版本好写，不管了以后有空再补


#输入
print("Please enter the original tuneer and the ambition tuneer(use space splite)")
tuneer = input("The default is to C:")

'''#b表示低音，#表示升（半音阶），g表示高音，用b#表示低半音，用g#表示高半音'''
putin = input("please enter number:")
first1 = ""
listin1 = []
listin2 = []
listout1 = []
listout2 = []
listoutTemp = []
listTemp = []
changekey = {}
changekey2 = {}

# #如有空格去除后再操作
# first1 =""
# listin1 = []
# listin2 = []
# listout1 = []
# first1 = putin.strip()
# final1 = first1.split(" ")
# for i in final1:
	# listin1.append(i)
# print(listin1)

# #对tune去除
# first2 =""
# first2 = tuneer.strip()
# final2 = first2.split(" ")
# for i in final2:
	# listin2.append(i)
# print(listin2)

#清除空格和转换大小写，默认到c调
def checkspace(listin):
	'''#b表示低音，#表示升（半音阶），g表示高音，用b#表示低半音，用g#表示高半音'''
	listTemp = ""
	listTemp = listin.strip()
	listlow = listTemp.lower()
	listOut = listlow.split(" ")
	if len(listOut) == 1:
		listOut.append("c")
	return listOut
	
#获取原始输入
listin1 = checkspace(putin)

formtuneer = checkspace(tuneer)

tuneerin = formtuneer[0]

tuneerout = formtuneer[1]

#b表示低音，#表示升（半音阶），g表示高音，用b#表示低升半音，用g#表示高半音
	
#keys	
GtoC = {"1" : "b5", "2" : "b6", "3" : "b7", "4" : "1", "5" : "2", "6": "3", "7" : "#4", "g1" : "5", "g2":"6","g3":"7","g4":"g1","g5":"g2","g6":"3","g7":"g#4","gg1":"g5"}
AtoC = {"b7" : "#5", "1" : "b6", "2" : "b7", "3" : "#1", "4" : "2", "5" : "3", "6" : "#4", "7" : "#5", "g1" : "6", "g2" : "7", "g3" : "g#1", "g4" : "g2", "g5" : "g3", "g6" : "g#4" }
BtoC = {"b6" : "b#5", "b7":"b#6", "1" : "b7", "2" : "#1", "3" : "#2", "4" : "3", "5" : "#4", "6" : "#5", "7" : "#6", "g1" : "7", "g2" : "g#1", "g3" : "g#2", "g4" : "g3", "g5" : "g#4"}
DtoC = {"b4" : "b5", "b5" : "b6", "b6" : "b7", "b7" : "#1", "1" : "2", "2" : "3", "3" : "#4", "4" : "5", "5" : "6", "6" : "7", "7" : "g#1", "g1" : "g2", "g3" : "g#4", "g4" : "g5"}
EtoC = {"b3" : "b#5", "b4" : "b6", "b5" : "b7", "b6" : "#1", "b7" : "#2", "1" : "3", "2" : "#4", "3" : "#5", "4" : "6", "5" : "7", "6" : "g#1", "7" : "g#2", "g1" : "g3", "g2" : "g#4"}
FtoC = {"b2" : "b5", "b3" : "b6", "b4" : "b#6", "b5" : "1", "b6" : "2", "b7" : "3", "1" : "4", "2" : "5", "3" : "6", "4" : "#6", "5" : "g1", "6" : "g2", "7" : "g3", "g1" : "g4", "g2" : "g5"}

Fulltunekey = {"g":GtoC, "a" : AtoC, "b" : BtoC, "d" : DtoC, "e" : EtoC, "f" : FtoC}

#Anykeys，key转换
def inverse(dict):
	dictout = {v : k for k,v in dict.items()}
	return dictout

CtoG = inverse(GtoC)
CtoA = inverse(AtoC)
CtoB = inverse(BtoC)
CtoD = inverse(DtoC)
CtoE = inverse(EtoC)
CtoF = inverse(FtoC)

Fulltuneanykey = {"g" : CtoG, "a" : CtoA, "b" : CtoB, "d" : CtoD, "e" : CtoE, "f" : CtoF}

#转换key-values对 （first 全到C)
def dictoc(tuneerin,tuneerout):
	if tuneerin == "a":
		changekey = Fulltunekey["a"]
	elif tuneerin == "g":
		changekey = Fulltunekey["g"]
	elif tuneerin == "b":
		changekey = Fulltunekey["b"]
	elif tuneerin == "d":
		changekey = Fulltunekey["d"]
	elif tuneerin == "e":
		changekey = Fulltunekey["e"]
	elif tuneerin == "f":
		changekey = Fulltunekey["f"]
	return changekey
# def dicany(tuneerin,tuneerout):
	# if tuneerin != "c":
		# changekey = Fulltunekey[tuneerin]
		
#判断输出，如不是C，再进行转换
def dictoany(tuneerout):
	if tuneerout == "a":
		changekey2 = Fulltuneanykey["a"]
	elif tuneerout == "g":
		changekey2 = Fulltuneanykey["g"]
	elif tuneerout == "b":
		changekey2 = Fulltuneanykey["b"]
	elif tuneerout == "d":
		changekey2 = Fulltuneanykey["d"]
	elif tuneerout == "e":
		changekey2 = Fulltuneanykey["e"]
	elif tuneerout == "f":
		changekey2 = Fulltuneanykey["f"]
	return changekey2		

def alltoC(tuneerin):
	changekey = dictoc(tuneerin, tuneerout)
	for i in listin1:
		listout1.append(changekey[i])
	#print(listout1)
	return listout1

# print(listout1)

def ctoall(tuneerout):
	if tuneerout != "c":
		changekey2 = dictoany(tuneerout)
		for i in listout1:
			listout2.append(changekey2[i])
	return listout2

# ctoall(tuneerout)
# print(listout2)	
	
# if tuneerout != "c":
	# dicany(tuneerout)
	# for i in listoutTemp:
		# listout1.append(changekey[i])
	# print(listout1)

#最后输出	
def checkout(tuneerin,tuneerout):
	if tuneerout == "c":
		alltoC(tuneerin)
		print(tuneerin,listin1)
		print("->")
		print("c",listout1)	
	else:
		listout2 = ctoall(tuneerout)
		print(tuneerin,listin1)
		print("->")
		print(tuneerout,listout2)
	return


checkout(tuneerin,tuneerout)
#AtoC = {"b7" : "#5", "1" : "b6", "2" : "b7", "3" : "#1", "4" : "2", "5" : "3", "6" : "#4", "7" : "#5", "g1" : "6", "g2" : "7", "g3" : "g#1", "g4" : "g2", "g5" : "g3", "g6" : "g#4" }
# if tuneerout == "c":
	# for i in listin1:
		# listout1.append(changekey[i])
	# print(listout1)
