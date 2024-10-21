#!/usr/local/bin/python
# Connect to MariaDB Platform
import mysql.connector #mariadb 執行套件
		#導入connector物件以連接DB
try:
	#連線DB
	conn = mysql.connector.connect(  
		user="root",		 #DB預設的帳號名稱	
		password="",	 	 #DB預設的帳號密碼（空）	
		host="localhost",    #代表資料庫放在哪個電腦上 
		port=3306,			 #mysql預設3306
		database="test"
	)
	#建立執行SQL指令用之cursor, 設定傳回dictionary型態的查詢結果 [{'欄位名':值, ...}, ...]
	cursor=conn.cursor(dictionary=True)  
	#cursor概念為資料庫中有一指標，指標可拿來執行sql指令，可從他取回查詢結果

except mysql.connector.Error as e: # mariadb.Error as e: 錯誤物件
	print(e) #這裡門處理錯誤 只是印出來
	print("Error connecting to DB")
	exit(1)  #中斷 ()數字隨意

def add(Jname,Jcon,dDay):
	sql="insert into todolist1 (jobname,jobcontent,status,dueDate) values(%s,%s,%s,%s)" #代表未來要套用的資料
	param=(Jname,Jcon,dDay,0) #注意後面"，" 當只有一的時候後面，才會被當list 。如果多個就不用
	cursor.execute(sql,param) #用前面sql指令，裡面的值用param的帶進去 
	conn.commit()
	return

def setfinish(id):
	sql="update todolist1 set status=1 where id=%s" #代表未來要套用的資料
	param=(id,) #注意後面"，" 當只有一的時候後面，才會被當list 。如果多個就不用
	cursor.execute(sql,param) #用前面sql指令，裡面的值用param的帶進去 
	conn.commit()
	return
	
def delete(id):
	sql="delete from todolist1 where id=%s; "
	param=(id,) #注意後面"，" 當只有一的時候後面，才會被當list 。如果多個就不用
	cursor.execute(sql,param)
	#cursor.execute(sql,(id,))
	conn.commit() #要commit出去才會寫到DB
	return

def update(id,data):
	sql="update 表格 set 欄位=值,... where 條件"
	#param=('值',...)
	cursor.execute(sql,param)
	conn.commit()
	return
	
def getList():
	sql="select id,jobname,jobcontent,status,dueDate from todolist1 ;"
	#param=('值',...)
	cursor.execute(sql) #查詢結果回傳回去CALL我的這個人
	return cursor.fetchall() #把結果全部印出來
