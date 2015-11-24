#!/usr/bin/python
from validate_email import validate_email
import os 

def stringToIntArray(indexs):
	if indexs=="":
		return []
	else:
		return map(int, indexs.split(" "))

def displayLine(item, idemail, indexs):
	i = -1
	for index in indexs:
		i+=1
		if index == idemail:
			p = "["+str(idemail)+"] %40s "% item[0].encode('string_escape')
		else:
			p+= " ["+str(index)+"] : " + item[i].encode('string_escape')
	return p


filename  = raw_input("Enter filename : ")
seperator = raw_input("Enter data seperator [,]: ")

indexs    = raw_input("Enter selected indexs (seperate by a single space): ")
indexs    = stringToIntArray(indexs)

idemail   = raw_input("Enter email index in file (blank for no email check): ")
idemail   = int(idemail)

not_blank_indexs = raw_input("Enter non blank check indexs (blank for no blan check): ")
not_blank_indexs = stringToIntArray(not_blank_indexs)

print "Dump : %s" %filename
print "Id Email : %s" %idemail

try:
	f = open(filename, 'r')
except:
	print "Error in handling file %s"%filename
	os._exit(-1)



user = 0
result = {}


line = f.readline()
while line!="":
	array = line.split(seperator)
	if idemail!="":
		is_valid = validate_email(array[idemail])
	else:
		is_valid = True

	if is_valid:
		is_selected=True
		for index in not_blank_indexs:
			if array[index] == "<blank>" or array[index]=="":
				is_selected=False
				break


	if is_valid and is_selected:
		user=user+1
		domaine=array[idemail].split("@")[1].encode('string_escape')

		entry = []
		for index in indexs:
			entry.append(array[index])


		try:
			result[domaine.lower()].append(entry)
		except:
			result[domaine.lower()]=[entry]

	line=f.readline()


#Display all domaines
i = 0
for domaine in result:
	i+=1
	print "%3s : " %i + domaine

for domaine in result:
	print "[domaine : ] " + domaine

	nbemail=0

	for item in result[domaine]:
		print displayLine(item, idemail, indexs)
		nbemail+=1
	print "=============================== %s ===========================" % nbemail

print "Total %s"%user