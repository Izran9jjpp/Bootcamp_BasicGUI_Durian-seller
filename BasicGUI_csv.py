#BasicGUI.py

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime , timedelta
import csv

####################

def timestamp(thai=True):
	if thai == True:
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543) #ทำให้เป็นพ.ศ.
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	return stamp


def writetext(quantity,total):
	#stamp = datetime.now()
	#stamp = stamp.replace(year=stamp.year+543) #ทำให้เป็นพ.ศ.
	#stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	stamp = timestamp
	filename = 'data1.txt'
	with open(filename,'a',encoding = 'utf-8') as file:
		file.write('\n' + 'วันที่-เวลา:{} ทุเรียน:{} kg ยอดรวม:{:,.2f} Bath' .format(stamp,quantity,total))


def wrcsv(data):
	# data  = ['Time',10,500]
	with open('data.csv','a',newline='',encoding= 'utf-8')as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('Success') 

def recsv():
	with open('data.csv',newline='',encoding ='utf-8') as file:
		fr = csv.reader(file)
		data = list(fr)
	return data

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

	################

GUI = Tk()
GUI.geometry('600x900')
GUI.title('Software by JJPP')

file = PhotoImage(file='dur.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text = 'Program calculation price of Durian',font=('Cordia New',30,'bold'),fg='green')
L1.pack() #.place)x,y), .grid(row=x,column=y)


L2 = Label(GUI,text = 'Please insert weight of durian',font=('cordia New',30),fg='blue')
L2.pack()

v_quantity = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impact',20))
E1.pack()

def Calcualte(event):
	quantity = v_quantity.get()
	price = 130
	print('price',float(quantity)*price)
	cal = float(quantity)*price
	
	# writetext(quantity,cal)

	# build .csv file
	data = [timestamp(),quantity,cal]
	wrcsv(data)
	smm = sumdata()
	title = 'Total pay'
	text1 = 'Price of durian today \nAmount of durian {} kg Total price: {:,.2f} Bath'.format(quantity,cal)
	messagebox.showinfo(title,text1)
	v_quantity.set('') #set E1 to ''
	E1.focus() #set cursor to 0 position


B1 = ttk.Button(GUI,text='Calculate',command=Calcualte)
B1.pack(ipadx=30,ipady=20,pady=20)
E1.bind('<Return>',Calcualte)


####pop up for total sell #####
def summaryData(event):
	smm = sumdata()
	title = 'Grand Total'
	text1 = 'Total amount of durian {} kg Total bill: {:,.2f} Bath'.format(smm[0],smm[1])
	messagebox.showinfo(title,text1)

GUI.bind('<F1>',summaryData)

E1.focus()

GUI.mainloop()


