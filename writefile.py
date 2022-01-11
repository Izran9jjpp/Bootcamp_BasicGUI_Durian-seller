from datetime import datetime

def writetext(quantity,total):
	stamp = datetime.now()
	stamp = stamp.replace(year=stamp.year+543) #ทำให้เป็นพ.ศ.
	stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	filename = 'data1.txt'
	with open(filename,'a',encoding = 'utf-8') as file:
		file.write('\n' + 'วันที่-เวลา:{} ทุเรียน:{} kg ยอดรวม:{:,.2f} Bath' .format(stamp,quantity,cal))
