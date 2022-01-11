#BasicGUI.py

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime , timedelta


GUI = Tk()
GUI.geometry('600x900')
GUI.title('Software by JJPP242526')

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

def Calcualte():
	quantity = v_quantity.get()
	price = 130
	print('price',float(quantity)*price)
	cal = float(quantity)*price
	#EN Date
	stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#Thai Date
	stamp = datetime.now() + timedelta(days=198327)
	stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')


	#correct qualtity to data1.txt
	filename = 'data1.txt'
	with open(filename,'a',encoding = 'utf-8') as file:
		file.write('\n' + 'วันที่-เวลา:{} ทุเรียน:{} kg ยอดรวม:{:,.2f} Bath' .format(stamp,quantity,cal))
	messagebox.showinfo('Price of durian','Amount of durian {} kg Total price: {:,.2f} Bath'.format(quantity,cal))

B1 = ttk.Button(GUI,text='Calculate',command=Calcualte)
B1.pack(ipadx=30,ipady=20,pady=20)




GUI.mainloop()


