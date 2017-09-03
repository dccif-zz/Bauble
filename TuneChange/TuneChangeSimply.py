
GtoC = {"1" : "b5", "#1" : "b#5", "2" : "b6", "#2" : "b#6", "3" : "b7", "4" : "1", "#4" : "#1", "5" : "2","#5" : "#2", "6": "3", "#6" : "4", "7" : "#4", "g1" : "5", "g#1" : "#5", "g2":"6", "g#2" : "#6", "g3":"7", "g4":"g1", "g#4" : "g#1","g5":"g2", "g#5" :"g#2", "g6":"g3","g#6" :"g4", "g7":"g#4","gg1":"g5"}
AtoC = {"b#6": "b5", "b7" : "#5", "1" : "b6", "#1" :"b#6", "2" : "b7", "#2" : "1", "3" : "#1", "4" : "2", "#4":"#2", "5" : "3","#5" : "4", "6" : "#4","#6":"5", "7" : "#5", "g1" : "6", "g#1" : "#6", "g2" : "7","g#2": "g1", "g3" : "g#1", "g4" : "g2", "g#4": "g#2", "g5" : "g3", "g#5": "g4", "g6" : "g#4","g#6":"g5" }
BtoC = {"b#5" : "b5","b6" : "b#5", "b#6" :"b6","b7":"b#6", "1" : "b7", "#1":"1", "2" : "#1", "#2":"2","3" : "#2", "4" : "3", "#4": "4", "5" : "#4","#5":"5", "6" : "#5","#6":"6", "7" : "#6", "g1" : "7","g#1":"g1", "g2" : "g#1", "g#2":"g2", "g3" : "g#2", "g4" : "g3","g#4":"g4", "g5" : "g#4","g#5":"g5"}
DtoC = {"b4" : "b5", "b#4":"b#5", "b5" : "b6", "b#5":"b#6","b6" : "b7", "b#6":"1","b7" : "#1", "1" : "2", "#1":"#2","2" : "3", "#2":"4", "3" : "#4", "4" : "5","#4":"#5", "5" : "6","#5":"#6", "6" : "7","#6":"g1", "7" : "g#1", "g1" : "g2", "g#1":"g#2", "g2":"g3","g#2":"g4", "g3" : "g#4", "g4" : "g5"}
EtoC = {"b#2":"b5","b3" : "b#5", "b4" : "b6","b#4":"b#6", "b5" : "b7", "b#5":"1","b6" : "#1", "b#6":"2","b7" : "#2", "1" : "3", "#1":"4","2" : "#4","#2":"5", "3" : "#5", "4" : "6", "#4":"#6","5" : "7", "#5":"g1","6" : "g#1", "#6":"g2", "7" : "g#2", "g1" : "g3","g#1":"g4", "g2" : "g#4","g#2":"g5"}
FtoC = {"b2" : "b5","b#2":"b#5", "b3" : "b6", "b4" : "b#6","b#4":"b7", "b5" : "1", "b#5":"#1","b6" : "2", "b#6":"#2","b7" : "3", "1" : "4","#1":"#4", "2" : "5","#2":"#5", "3" : "6", "4" : "#6", "#4":"7","5" : "g1", "#5":"g#1","6" : "g2", "#6":"g#2","7" : "g3", "g1" : "g4", "g#1":"g#4","g2" : "g5"}

Fulltunekey = {"g":GtoC, "a" : AtoC, "b" : BtoC, "d" : DtoC, "e" : EtoC, "f" : FtoC}

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
	
def ctoall(tuneerout):
	if tuneerout != "c":
		changekey2 = dictoany(tuneerout)
		listout1 = alltoC(tuneerin)
		for i in listout1:
			listout2.append(changekey2[i])
	return listout2
	
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
