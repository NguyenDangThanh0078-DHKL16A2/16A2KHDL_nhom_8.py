nv = [{'Mã nhân viên':'nv1','Tên nhân viên':'Nam','Lương ngày':10,'Ngày công':26,'Lương tháng':1,'Thưởng':1},{'Mã nhân viên':'nv2','Tên nhân viên':'Hào','Lương ngày':20,'Ngày công':2,'Lương tháng':1,'Thưởng':1}]
# nv = [{'Mã nhân viên':'nv001','Tên nhân viên':'thiên bảo','Lương ngày':250.0,'Ngày công':29,'Lương tháng':720.0,'Thưởng':1000}]
def in_danh_sach():
	print('+','{:-^12}'.format(''),'+','{:-^20}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+')
	print('|','{:^12}'.format('Mã nhân viên'),'|','{:^20}'.format('Tên nhân viên'),'|','{:^12}'.format('Lương ngày'),'|','{:^12}'.format('Ngày công'),'|','{:^12}'.format('Lương tháng'),'|','{:^12}'.format('Thưởng'),'|')
	for i in nv:
		print('|','{:^12}'.format(i['Mã nhân viên']),'|','{:^20}'.format(i['Tên nhân viên']),'|','{:^12}'.format(i['Lương ngày']),'|','{:^12}'.format(i['Ngày công']),'|','{:^12}'.format(i['Lương tháng']),'|','{:^12}'.format(i['Thưởng']),'|')
	print('+','{:-^12}'.format(''),'+','{:-^20}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+')
def them_nv():
	print('{:+^99}'.format(' THÊM NHÂN VIÊN '))
	ma_nv = input('Nhập mã nhân viên mới:')
	ten_nv = input('Nhập tên nhân viên:')
	luong_ngay = float(input('Nhập lương ngày:'))
	ngay_cong = int(input('Nhập ngày công:'))
	luong_thang = luong_ngay*ngay_cong
	if ngay_cong < 22:
		thuong = 1000
	elif ngay_cong < 24:
		thuong = 2000
	elif ngay_cong < 26:
		thuong = 3000
	else:
		thuong = 5000
	nv.append({'Mã nhân viên':ma_nv,'Tên nhân viên':ten_nv,'Lương ngày':luong_ngay,'Ngày công':ngay_cong,'Lương tháng':luong_thang,'Thưởng':thuong})
	in_danh_sach()

def tim_nv():
	l =[]
	print('{:-^99}'.format('TÌM NHÂN VIÊN'))
	d = input('Nhập tên nhân viên bạn muốn tìm:')
	def check():
		for i in range(len(nv)):
			if nv[i]['Tên nhân viên'] == d:
				e1 = i
				break
			else:
				e1 = -1
		return e1
	e2 = check()
	if e2 == -1:
		print('Không tồn tại nhân viên tên',d,'!')
	else:
		print('+','{:-^12}'.format(''),'+','{:-^20}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+')
		print('|','{:^12}'.format('Mã nhân viên'),'|','{:^20}'.format('Tên nhân viên'),'|','{:^12}'.format('Lương ngày'),'|','{:^12}'.format('Ngày công'),'|','{:^12}'.format('Lương tháng'),'|','{:^12}'.format('Thưởng'),'|')
		print('|','{:^12}'.format(nv[e2]['Mã nhân viên']),'|','{:^20}'.format(nv[e2]['Tên nhân viên']),'|','{:^12}'.format(nv[e2]['Lương ngày']),'|','{:^12}'.format(nv[e2]['Ngày công']),'|','{:^12}'.format(nv[e2]['Lương tháng']),'|','{:^12}'.format(nv[e2]['Thưởng']),'|')
		print('+','{:-^12}'.format(''),'+','{:-^20}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+')



def xoa_nv():
	print('{:-^100}'.format(' XÓA NHÂN VIÊN '))
	in_danh_sach()
	e = input('Nhập mã nhân viên muốn xóa: ')
	def check():
		for i in range(len(nv)):
			if nv[i]['Mã nhân viên'] == e:
				e1 = i
				break
			else:
				e1 = -1 
		return e1
	e2 = check()
	if e2 == -1:
		print('Không có mã nhân viên này')
		control()
	else:
		b = 1 
		while b != 0:
			print('+','{:-^12}'.format(''),'+','{:-^20}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+')
			print('|','{:^12}'.format('Mã nhân viên'),'|','{:^20}'.format('Tên nhân viên'),'|','{:^12}'.format('Lương ngày'),'|','{:^12}'.format('Ngày công'),'|','{:^12}'.format('Lương tháng'),'|','{:^12}'.format('Thưởng'),'|')
			print('|','{:^12}'.format(nv[e2]['Mã nhân viên']),'|','{:^20}'.format(nv[e2]['Tên nhân viên']),'|','{:^12}'.format(nv[e2]['Lương ngày']),'|','{:^12}'.format(nv[e2]['Ngày công']),'|','{:^12}'.format(nv[e2]['Lương tháng']),'|','{:^12}'.format(nv[e2]['Thưởng']),'|')
			print('+','{:-^12}'.format(''),'+','{:-^20}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+','{:-^12}'.format(''),'+')
			print('{:?^99}'.format(' Bạn có chăc chắn muốn xóa nhân viên này '))
			print('{:^99}'.format('1.Xóa      2.Không'))
			e3 = input('Entry your choose:')
			if e3 == '1':
				nv.pop(e2)
				print('Đã xóa nhân viên có mã:',e)
				back()
			elif e3 =='2':
				control()
			else:
				b = 1

def tinh_luong():
	for i in range(len(nv)):
		nv[i]['Lương tháng'] = nv[i]['Lương ngày']*nv[i]['Ngày công']
	return nv

def tinh_thuong():
	for i in nv:
		if i['Ngày công'] < 22:
			i['Thưởng'] = 1000
		elif i['Ngày công'] < 24:
			i['Thưởng'] = 2000
		elif i['Ngày công'] < 26:
			i['Thưởng'] = 3000
		else:
			i['Thưởng'] = 5000
	
def luu_file():
	while True:
		print('{:?^99}\n'.format(' Bạn muốn lưu '))
		print('{:^99}'.format('1.Lưu        2.Trở lại'))
		f1 = input('Entry your choose:')
		if f1 == '1':
			import csv
			f = open('files/ds_luong_nv.csv','w',newline='',encoding='utf-8')
			csv.writer(f).writerow(['Mã nhân viên','Tên nhân viên','Lương ngày','Ngày công','Lương tháng','Thưởng'])
			for row in nv:
				csv.writer(f).writerow([row['Mã nhân viên'],row['Tên nhân viên'],row['Lương ngày'],row['Ngày công'],row['Lương tháng'],row['Thưởng']])
			f.close()
			print('Đã lưu')
			break
		elif f1 == '2':
			control()
		else:
			print('Nhập 1 or 2')

def mo_file():
	try:
		nv.clear()
		import csv
		with open('files/ds_luong_nv.csv','r',encoding='utf-8') as f:
			reader = csv.reader(f)
			for row in reader:
				if row[0] == 'Mã nhân viên':
					continue
				nv.append({'Mã nhân viên':row[0],'Tên nhân viên':row[1],'Lương ngày':row[2],'Ngày công':row[3],'Lương tháng':row[4],'Thưởng':row[5]})		
			print('Đã mở')
			return(nv)
	except :
		print('\n')	

def sap_sep():
	l = {}
	n = []
	ss = []
	for i in range(len(nv)):
		l[i] = nv[i]['Ngày công']
		iteam_sorted = sorted(l.items(),key = lambda x: x[1])
	for i in range(len(iteam_sorted)):
		n.append(iteam_sorted[i][0])
		n.reverse()
	for i in n:
		ss.append(nv[i])
	nv.clear()
	for i in ss:
		nv.append(i)
	return(nv)

#--------------------------------------------------------------------------------------------
def back():
	print('{:?^99}\n'.format(' Bạn có muốn tiếp tục '))
	print('{:^99}'.format('1.Tiếp tục        2.Thoát'))
	z = input('Entry your choose:')
	if z == '1':
		control()
	elif z == '2':
		print('Xin cảm ơn')
	else:
		print('Hãy nhập lại!!')
		back()

#----------------------------------------------------------------------------------------------------------------
def welcome():
	print('{:^100}'.format(' 1.Xem lương nhân viên '))
	print('{:^100}'.format('2.Thêm nhân viên'))
	print('{:^100}'.format('3.Tìm nhân viên'))
	print('{:^100}'.format('4.Xóa nhân viên'))
	print('{:^100}'.format('5.Tính lương nhân viên'))
	print('{:^100}'.format('6.Tính thưởng'))
	print('{:^100}'.format('7.Mở file danh sách nhân viên'))
	print('{:^100}'.format('8.Lưu danh sách nhân viên'))
	print('{:^100}'.format('9.Sắp xếp thưởng'))
	try:
		entry = int(input('Entry your choose:'))
	except:
		print('Hãy nhập lại!')
		control()
	return entry

def control():
	print('{:*^100}'.format('CHƯƠNG TRÌNH QUẢN LÝ NHÂN VIÊN'))
	print('\n')
	entry = welcome()
	if entry == 1:
		print('{:-^99}'.format('DANH SÁCH NHÂN VIÊN'))
		in_danh_sach()
		back()
	elif entry == 2:
		them_nv()
		back()
	elif entry == 3:
		tim_nv()
		back()
	elif entry == 4:
		xoa_nv()
		back()
	elif entry == 5:
		tinh_luong()
		in_danh_sach()
		back()
	elif entry == 6:
		tinh_thuong()
		in_danh_sach()
		back()
	elif entry == 7:
		mo_file()
		in_danh_sach()
		back()
	elif entry == 8:
		luu_file()
		back()
	elif entry == 9:
		sap_sep()
		in_danh_sach()
		back()
	else:
		print('Mời bạn nhập lại!')
		control()

control()