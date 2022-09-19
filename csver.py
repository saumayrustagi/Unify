import csv

def writeLst(tbw):
	with open('list.txt', 'w') as ls:
		ls.write(str(tbw))

with open("./csv/a1.csv") as file_name:
    file_read = csv.reader(file_name, delimiter=':')
    array = list(file_read)
    

writeLst(array)
