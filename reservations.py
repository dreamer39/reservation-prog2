import csv
from datetime import datetime , timedelta
number=0
def check_a_room(hotel_name):
	f1 = open('hotel list.csv', "rb")
	reading=list(csv.reader(f1,delimiter=','))
	for line in reading:
		if  hotel_name ==line[1]:
			index=line[0]
			if int(line[-1])>0:
				print 'there are',line[-1], 'rooms in the',hotel_name,'hotel.\n' 	
			else:
					print 'there are no empty rooms in the',hotel_name,'hotel.' 
					
def update_numbers_of_rooms(update,index):
	f1 = open('hotel list.csv', "rb")
	ff=csv.reader(f1,delimiter=',')
	l=list(ff)
	l[int(index)-1][-1]=update
	writing=csv.writer(open('hotel list.csv','wb'))
	for i in l:
		writing.writerow(i)
	f1.close()

def reserve_room (hotel_name,customer_first_name,customer_last_name):
	customer_full_name= customer_first_name +','+ customer_last_name
	f1 = open('hotel list.csv', "rb+")
	reading=list(csv.reader(f1,delimiter=','))
	for line in reading:
		if  hotel_name ==line[1]:
			index=line[0]
			if int(line[-1])>0:
				print 'there are',line[-1], 'rooms in the',hotel_name,'hotel.\n' 	
				asking=raw_input("Do u want to reserve a room in this hotel for mr/mrs "+str(customer_last_name)+' YES, NO ?\n')
				if asking in ['Yes','Y','y','yes','YES']:
					check_in_date=datetime.now().strftime('%d of %b 20%y %H:%M:%S')
					days_to_stay= raw_input('How many days to stay?')
					phone_number=int(raw_input("pls enter customer's phone number\n"))
					if phone_number>11 or phone_number<10:
						print 'please write 10digit number only'
						phone_number=int(raw_input("What is the customer's phone number\n"))
					reservation_related(hotel_name,customer_full_name,check_in_date,days_to_stay,phone_number)
					update=int(line[-1])-1
					update_numbers_of_rooms	(update,index)				
				elif asking in ['No','N','n','no','NO']:
					print ' '*10+'.'*50
					print ' '*30+ 'BACK TO HOME PAGE'
					print ' '*10+'.'*50
					welcome()
			else:
					print 'there are no empty rooms in the',hotel_name,'hotel...SORRY',customer_first_name

def add_new_reservation(hotel_name,customer_full_name,check_in_date,days_to_stay,check_out_date,phone_number):
	global number
	number=number+1
	hotel_id=''
	reservation_number=str(number)
	f1 = open('reservation list.csv', "rb")
	reading=list(csv.reader(f1,delimiter=','))	
	for line in reading:
		if line==[]:	
				reservation_number=str(number)	
				customer_id=str(number)
		else:				
			f1 = open('reservation list.csv', "rb")				
			last_count=line[0]
			if last_count>number:
				last_count=int(last_count)
				last_count+=1
				reservation_number=str(last_count)
				customer_id=str(last_count)
	f1.close()
	f1 = open('hotel list.csv', "rb")
	reading=list(csv.reader(f1,delimiter=','))	
	for line in reading:
		if line[1]==hotel_name:
			hotel_id=line[0]
			hotel_name=line[1]
	with open('reservation list.csv','ab') as writing:
		r=csv.writer(writing)
		r.writerow ([reservation_number,hotel_id,customer_id,check_in_date,days_to_stay,check_out_date])
	print ' '*20,'.'*50
	print ' '*25, 'thank u....reservation is confirmed...'
	print ' '*20,'.'*50
	add_customer(customer_full_name,phone_number)

def reservation_related(hotel_name,customer_full_name,check_in_date,days_to_stay,phone_number):
	check_out_date=(timedelta(int(days_to_stay))+datetime.now()). strftime('%d of %b 20%y %H:%M:%S')
	add_new_reservation(hotel_name,customer_full_name,check_in_date,days_to_stay,check_out_date,phone_number)	
		
def add_customer(customer_full_name,phone_number):
	two_names=customer_full_name.split(',')
	customer_first_name=two_names[0]
	customer_last_name=two_names[1]
	global number
	number=number+1
	customer_number=''
	f1 = open('reservation list.csv')
	reading=list(csv.reader(f1,delimiter=',', quotechar='"'))	
	for line in reading:
		if line==[]:
			customer_number=str(number)
		else:
			customer_number=line[0]			
	with open('customer list.csv','ab') as writing:
		r=csv.writer(writing)
		r.writerow ([customer_number,customer_first_name,customer_last_name,customer_full_name,phone_number])

def customer_related():
	customer_first_name=raw_input("What is the customer's first name\n")
	customer_last_name=raw_input("What is the customer's last name\n")
	customer_full_name= customer_first_name +','+ customer_last_name
	add_customer(customer_first_name,customer_last_name,customer_full_name,phone_number)

def add_hotel(hotel_name, city,total_rooms,empty_rooms):
	f1 = open('hotel list.csv', "rb")
	reading=list(csv.reader(f1,delimiter=','))
	global number
	number=number+1
	number_hotel=str(number)
	for line in reading:
		if line==[]:	
				number_hotel=str(number)			
		else:				
			f1 = open('hotel list.csv', "rb")
			last_count=reading[-1][0]
			if last_count>number:
				last_count=int(last_count)
				last_count+=1
				number_hotel=str(last_count)
	f1.close()
	with open('hotel list.csv','ab') as writing:
		r=csv.writer(writing)
		r.writerow ([number_hotel,hotel_name,city,total_rooms,empty_rooms])
	asking=raw_input('Do u want to add other hotels to database?...PLS WRITE YES,NO.....')
	print asking
	if asking in ['Yes','Y','y','yes','YES']:
		hotel_related()
	elif asking in ['No','N','n','no','NO']:
		writing.close()
		exit()

def hotel_related():
	hotel_name=raw_input('what is the hotel name\n')
	city=raw_input('What city is the hotel located?\n')
	total_rooms=str(raw_input('Enter total no. of rooms\n'))
	empty_rooms=str(raw_input('Enter Empty no. of rooms\n'))
	add_hotel(hotel_name, city,total_rooms,empty_rooms)
			
def search_by_city_or_hotel():
	global number
	searching=raw_input('search by city or hotel...\n')
	f1 = open('hotel list.csv', "rb")
	reading=list(csv.reader(f1,delimiter=','))
	result=number
	for line in reading:
			city=line [2]	
			name=line[1]
			if not city.find (searching ):
				result+=1
				print '\nSeaarch Results for Hotels in',searching
				print 'result no.',result
				print
				d={'hotel_id':line[0],'hotel_name':line[1],'hotel_location':line[2],'no. of total rooms':line[3],'no. of empty rooms':line[4]}
				for k in d:
					print k,':',d[k]	
			elif not name.find(searching):
				print '\nSeaarch Results for Hotel',searching
				print
				d={'hotel_location':line[2],'no. of total rooms':line[3],'no. of empty rooms':line[4]}
				for k in d:
					print k,':',d[k]
										
def list_resevrations_for_hotel(hotel_name):
	global number
	result=number
	f1 = open('hotel list.csv', "rb")
	reading=list(csv.reader(f1,delimiter=','))
	for line in reading:
			name=line[1]
			id=line[0]
			if name==hotel_name:
				f1 = open('reservation list.csv', "rb")
				reading=list(csv.reader(f1,delimiter=','))
				f1 = open('customer list.csv', "rb")
				readingc=list(csv.reader(f1,delimiter=','))
				for line in reading:
					if id in line[1]: 
						result+=1
						print '\nresult:',result
						print 
						for x in readingc:
							customer_name=x[3]
							customer_id=x[0]
							if customer_id in line[2]:
								d={'reservation_id':line[0],'hotel_name':name,'customer_name':customer_name,'check_in_date':line[3],'days_to_stay':line[4],'check_out_date':line[5] }
						for k in d:
							print k,':',d[k]
				if  id not in line[1]:
					print 'There Is No Reservation In This Hotel'

def welcome():	
	print ' '*10 , '*' *50
	welcom_sms="Helllo User Pls Welcom to D.com.."
	print ' '*20,welcom_sms,'\n'
	print ' '*10 , '*' *50
	print "1- Add New Reservations.\n"
	print "2- Add New Hotels to DataBase.\n"
	print "3- Check if room avilable.\n"
	print "4- Search Hotels in a city or Info About Specified Hotel\n"
	print '5- List Reservation In a Hotel\n'
	print '6- Exit'
	user_input=raw_input("\n write the number of your choice...\n")
	if user_input==str(1):
		hotel_name= raw_input('pls enter hotel name...\n')
		customer_first_name=raw_input('pls enter your first name...\n')
		customer_last_name=raw_input('pls enter your last name...\n')
		reserve_room (hotel_name,customer_first_name,customer_last_name)
	elif user_input==str(2):
		hotel_related()	
	elif user_input==str(3):
		hotel_name=raw_input('enter hotel name..')
		check_a_room(hotel_name)	
	elif user_input==str(4):
		search_by_city_or_hotel()
	elif user_input==str(5):
		hotel_name=raw_input('Enter hotel name...')
		list_resevrations_for_hotel(hotel_name)
	elif user_input==str(6):
		exit()
	else:
		print '\nSORRY...INVALID INPUT\npls write a number of your choice only'

		
making_hotel_list=open('hotel list.csv','a+')
making_customer_list=open('customer list.csv','a+')
making_reservation_list=open('reservation list.csv','a+')
welcome()

