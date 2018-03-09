import pymssql

ROOMid = range(100,141)
ROOMtype = [1,2,3,4,5,6]
ROOMfloor =['1','2','3','4','5']
ROOMface = ['N','E','W','S']
ROOMfeature = ['123']
SqlScentence="Insert into Room_Info VALUES('{roomid}','{roomfloor}'"
SqlScentence=SqlScentence.format(roomid=str(ROOMtype[0]),roomfloor=ROOMfloor[0])
print(SqlScentence)

# conn = pymssql.connect(server='ALIENWARE',user='Temp',password='123456',database='Hotel')
# cursor = conn.cursor()
#
# cursor.execute("INSERT into Room_Info VALUES ('13','2','1','N','123')")
# conn.commit()
# conn.close()
