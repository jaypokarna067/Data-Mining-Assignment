import csv

path1 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/Modified/quantity_modified/combined.csv"
path2 = "./profit_decSales.csv"
#path1 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/augSales.csv"
#path2 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/Modified/modified_augSales.txt"

prices_dic = {'1': '7', '2': '8', '3': '12', '4': '21', '5': '8', '6': '10', '12': '30', '14': '10', '15': '35', '16': '5', '18': '55', '19': '20', '20': '25', '21': '30', '22': '15', '23': '20', '24': '25', '25': '10', '26': '5', '41': '15', '45': '10', '46': '18', '47': '10', '48': '10', '49': '20', '50': '20', '51': '15', '54': '20', '73': '30', '74': '25', '76': '33', '93': '32', '94': '14', '98': '10', '99': '10', '100': '35', '102': '10', '103': '10', '104': '10', '105': '25', '107': '10', '108': '20', '123': '8', '124': '25', '125': '35', '126': '40', '127': '55', '128': '25', '129': '16', '130': '21', '131': '21', '132': '21', '133': '21', '134': '15', '135': '21', '136': '25', '137': '30', '138': '22', '139': '21', '140': '26', '141': '40', '142': '25', '143': '16', '144': '20', '145': '40', '146': '85', '147': '75', '148': '90', '149': '3', '150': '6', '151': '12', '152': '15', '153': '17', '154': '22', '155': '27', '156': '30', '157': '32', '158': '14', '159': '20', '160': '25', '161': '12', '162': '18', '163': '20', '164': '81', '165': '30', '166': '85', '167': '10', '168': '27', '169': '25', '170': '20', '171': '20', '172': '80', '173': '45', '174': '12', '175': '18', '176': '30', '177': '95', '178': '40', '179': '23', '180': '170', '181': '10', '182': '95', '183': '20', '184': '25', '185': '25', '186': '18', '187': '15', '188': '18', '189': '12', '190': '15', '191': '20', '192': '20', '193': '18', '194': '10', '195': '35', '196': '25', '197': '2', '198': '20', '900': '100', '901': '-100', '902': '25', '903': '5'}
maindic = {'2': ({17}, {'F2'}), '151': ({20, 21, 22, 23}, {'F1', 'F2', 'F0', 'F4', 'F3'}), '128': ({0, 21, 22, 23}, {'F1', 'F2', 'F4', 'F3'}), '130': ({20}, {'F0'}), '123': ({17}, {'F2'}), '154': ({0, 20, 21, 22, 23}, {'F1', 'F2', 'F4', 'F3'}), '134': ({0, 23}, {'F1', 'F2', 'F3'}), '146': ({20}, {'F0'}), '169': ({0, 21, 22}, {'F2'})}

'''secondary_list = [
('151',21, 'F3'), 
('134',0, 'F3'),
('2',17, 'F2'),
('154',23, 'F3'),
('154',22, 'F2'),
('151',23, 'F2'),
('76',22, 'F2'),
('128',0, 'F2'),
('151',18, 'F2'),
('151',0, 'F3'),
('154',20, 'F2'),
('151',20, 'F3'),
('128',22, 'F2'),
('123',17, 'F2'),
('154',23, 'F4'),
('134',23, 'F2'),
('151',22, 'F3'),
('151',20, 'F4'),
('154',0, 'F3'),
('134',1, 'F2'),
('128', 23, 'F2'),
('134', 23, 'F3')
]'''




segment_wt = {'F1': 12, 'F2': 32, 'F3': 30, 'F4': 20, 'F5': 3, 'H1': 2, 'H2': 20, 'P5':1, 'F6':1, 'B1':1, 'H4':1, 'F7':1, 'D1':1, 'H3':1, 'P3':1, 'P1':1, 'P2':1}

missing = 0
total_revenue = 0
total_revenue_orig = 0
minute_partition = 59

def get_penalty():
	ans = 0
	'''for t in secondary_list:
		price_change = min(int(prices_dic[t[0]])*.1, 10)
		seg_wt = '''


	
	ans = 0
	for key, val in maindic.items():
		seg_wt_total = 0
		for seg in val[1]:
			if(seg == 'F0'):
				continue
			seg_wt_total += segment_wt[seg]
		total_hours = len(val[0])**2
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		price_change = min(int(prices_dic[key])*.1, 10)
		ans += price_change * total_hours * seg_wt_total
	return ans

def formula(item, hr, grp, price):
	if(str(item) not in maindic):
		return 0
		
	if((int(hr) in maindic[str(item)][0]) and (grp in maindic[str(item)][1])):
		'''print('min =', min(price*0.1, 10))'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		return min(price*.1, 10)
	else:
		return 0
	
with open(path1,'rt',encoding="latin1") as csvfile:
	r = csv.reader((x.replace('\0', '') for x in csvfile), delimiter='\t')

	count = 0
	total = 0
	flag = True
	for row in r:
		total += 1
##		print(row)
##		input()
		if flag:
			flag = False
			continue
		if(row[1] == '151' and row[8] == 'F0' and str(row[9]) == '21'):
					count += 1
	print((count/total)*100)
