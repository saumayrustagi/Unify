#Assuming standardized array is called A1.
import csv
import mysql.connector
import ast

def readLst():
	with open('list.txt') as f:
		data = f.read()
	d = ast.literal_eval(data)
	return d

tablename="trial21"
#connect() method established a connection to the MySQL database from Python application and returned a MySQLConnection object
con=mysql.connector.connect(host="localhost", user="root", password="sandyserver",database="diabolical")

#This method returns a cursor object. Using a cursor object, we can execute SQL queries.
#Cursor objects interact with the MySQL server using a MySQLConnection object.
mycursor=con.cursor()

A1 = readLst()

ls=[]
i=0

print(A1)

while i<len(A1):
	ls.append(A1[i][0])
	i+=1



while i<len(A1):
	ls.append(A1[i][0])
	i+=1

print(ls)

flag = 0
count=0
for i in A1:
	for j in i:
		print(j)
		if j in ls:
			x=j
			flag=1
			continue
		if flag==1 and count==0:
			sql0="Create table %s(%s varchar(25))"%(tablename,x)
			mycursor.execute(sql0)
			con.commit()
			sql="INSERT INTO %s(%s) VALUES('%s')"%(tablename,x,j)
			mycursor.execute(sql)
			con.commit()
			c1=x
			v1=j
			flag=0
			count=count+1
			continue
		if flag==1 and count>=1:
			# ~ print("WHY %s %s"%(x,j))
			
			sql0="ALTER table %s add column %s varchar(25)"%(tablename,x)
			mycursor.execute(sql0)
			con.commit()
			
			sql="UPDATE %s set %s = '%s' WHERE %s='%s'"%(tablename,x,j,c1,v1)
			mycursor.execute(sql)
			con.commit()
		
			count=count+1;
			flag=0
			continue
