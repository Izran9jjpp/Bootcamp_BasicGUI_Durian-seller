#write CSV file

import csv

def wrcsv(data):
	# data  = ['Time',10,500]
	with open('data.csv','a',newline='',encoding= 'utf-8')as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('Success')

# d = ['2022-01-05 23:34:24',50,500]
# wrcsv(d)


def recsv():
	with open('data.csv',newline='',encoding ='utf-8') as file:
		fr = csv.reader(file)
		data = list(fr)
	return data


result = recsv()

#show list
sumlist_q = []
for d in result:
	sumlist_q.append(float(d[1]))

print(sumlist_q,sum(sumlist_q))

#short
sumlist_q2 = [float(s[1]) for s in result]
print(sumlist_q2,sum(sumlist_q2))

#shorter
sumlistq3 = sum([float(t[1]) for t in result])
print(sumlistq3)

def sumdata():
	result = recsv()
	sumlist_q = []
	sumlist_tt = []
	for d in result:
		sumlist_q.append(float(d[1]))
		sumlist_tt.append(float(d[2]))
	sumq = sum(sumlist_q)
	sumtt = sum(sumlist_tt)

	return(sumq,sumtt)

res = sumdata()
print(res)



# def recsv():
# 	with open('data.csv',newline='',encoding ='utf-8') as file:
# 		fr = csv.reader(file)
# 		print(list(fr))
	
# recsv()




