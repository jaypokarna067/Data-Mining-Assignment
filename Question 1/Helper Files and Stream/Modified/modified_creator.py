import csv


path1 = "../novSales.csv"
path2 = "./modified_novSales.csv"
#path1 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/augSales.csv"
#path2 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/Modified/modified_augSales.txt"

missing = 0

minute_partition = 59

def getnexthour(hour):
	if(hour == 23):
		return str(0)
	return str(hour+1)

def gethour(x):
	x = (x.split(' '))[1]
	hour = x.split(':')[0]
	minute = x.split(':')[1]

	if(int(minute) > minute_partition):
		return getnexthour(int(hour))
	else:
		return int(hour)

with open(path1,'rt',encoding="latin1") as csvfile, open(path2, 'w', encoding="latin1") as modified:
	r = csv.reader(x.replace('\0', '') for x in csvfile)
	spamwriter = csv.writer(modified, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)

	count = 0
	flag = True
	for row in r:
		count += 1
		towrite = []
		for val in row:
			towrite.append(str(val)) #+ '\t'
			if val == '':
				missing += 1
		if(flag):
			flag = False
			towrite.append('student_group')
			towrite.append('hour')
		else:
#CURRENTLY FOR DEC SALES#CURRENTLY FOR DEC SALES#CURRENTLY FOR DEC SALES
#CURRENTLY FOR DEC SALES#CURRENTLY FOR DEC SALES#CURRENTLY FOR DEC SALES#CURRENTLY FOR DEC SALES
#CURRENTLY FOR DEC SALES#CURRENTLY FOR DEC SALES#CURRENTLY FOR DEC SALES
#CURRENTLY FOR DEC SALES#CURRENTLY FOR DEC SALES#CURRENTLY FOR DEC SALES
			towrite.append(row[5][:2])
			towrite.append(str(gethour(row[3])))
		#towrite += '\n'
		spamwriter.writerow(towrite)
		#if(count == 10):
			#break

	print(missing)
