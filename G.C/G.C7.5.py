# This is a very basic pogram that ask the user what type of grade they would like to input and only has one option, 
# individual grade calc. or test calc.

from ast import While
from audioop import add
#igc stands for individual grade calculator
#agc stands for average grade calculator

def test_calc(): # Function for igc calculator
	if total_ques >= missed_ques:
#The total num of question - missed question. This gives you the number of right answers and makes calculation easier. 
		ques_right = total_ques - missed_ques
		raw_score = ques_right / total_ques #Num of questions right divided by total questions gives a grade. 
		user_grade2 = raw_score *100 #This gives the grade as a percent. The user is more likely to recognize the grade this way.
		user_grade2 = round(user_grade2)
		print('Grade:', user_grade2)

def test(): # Funtion for test grades in agc 
	if t_d == ('t'): 
		add_tg = int(round(float(input('Add a test grade: '))))
# User inputs grade the grade, the grade is converted into a foat, rounded and changed into an int.
		if add_tg > 0 and add_tg <= 100: # Makes sure the user can only input grades 0 - 100
			tg_list.append(add_tg) # Adds the grade to the test grade list. 
			print (tg_list) # This is temporary and will not be in the final product, prints list.
		if add_tg > 100 or add_tg < 0: 
			# Gives the user an erroe if they input a number not in the range 0 - 100
			print ('number inputed not valid')

 
def test_average(): # Funtion for all the test grade averages.
	tg_sum = 0 # Initailizes the test grade sum to 0.
	for item in tg_list: # Gets the sum of the list. 
		tg_sum += (item)

	tg_average = tg_sum / len(tg_list) # Sum divided by length is the average. 

	return tg_average


def daily():
	if t_d == ('d'):
		add_dg = int(round(float(input('Add a daily grade: '))))
		if add_dg > 0 and add_dg <= 100:
			dg_list.append(add_dg)
			print (dg_list)
		if add_dg > 100 or add_dg < 0:
			print ('number inputted not valid')
		
def daily_average():
	dg_sum = 0
	for x in dg_list:
		dg_sum += (x)

	dg_average = dg_sum / len(dg_list)

	return dg_average

def average(): # Function for the total average.
	daily_average() # Calls the daily_average.
	test_average()	# Calls the test_average.
	t_sum = 0 # Initailize total sum to 0.
	d_sum = 0

	for x in tg_list: # Gets the sum of both lists. 
		t_sum += (x)
	
	for x in dg_list:
		d_sum += (x)
	
	print (t_sum)
	print (d_sum)

	raw_s = t_sum * d_sum / len(tg_list) # Divides the total sum by the length of both lists.

	if len(tg_list) <= 1 and len(dg_list) <= 1:
		raw_s = t_sum * d_sum /2
	
	if len(tg_list) >= 2 and len(dg_list) >= 2:
		raw_s = t_sum * d_sum / len(tg_list) # Divides the total sum by the length of both lists.
		ave1 = raw_s / len(tg_list)
		ave2 = ave1 / len(dg_list)
	return raw_s
	return ave2



home_screen = input('What would you like to do?(igc)(agc) ')
if home_screen == ('igc'): #Stands for individual grade calculator but is more like a test calculator.
	total_ques = int(input('Total questions: '))
	missed_ques = int(input('How many do you think you got wrong: '))
	test_calc()


if home_screen == ('agc'): #Agc stands for average grade calculation.
	agc = True #Intializes agc and gives a variable for the while loop to work with.
	tg_list = [] # Test grade list. 
	dg_list = [] # Daily grade list
	while agc == True: # Initializes agc to true. 
		add_grade = input('Would you like to add a grade(y,n): ') # Asks the user if they would like to add a grade.
		if add_grade == ('y'):
			t_d = input('Is a daily or test grade(d,t): ')

		while t_d == ('d'):
			daily() # Calls the daily grade function if the user inputs d. 
			add_grade = input('Would you like to add a grade(y,n): ')
			t_d = input('Is it a daily or test grade(d,t): ')

		while t_d == ('t'):
			test() # Calls the test grade function if the user unputs t. 
			add_grade = input('Would you like to add a grade(y,n): ')
			t_d = input('Is it a daily or test grade(d,t): ')

		if add_grade == ('n'):
			avg = input('get average? ')
			if avg == ('y'):
				print('test average: ', test_average())
				print('daily average: ', daily_average())
				print('your total is: ', average())
				agc = False
			else:
				agc = False











'''		test_daily = input('Is it a daily or test grade: ')
		if test_daily == ('test'):
			add_tg = int(input('Add a test grade: '))
			tg_list.append(add_tg)
			print (tg_list)'''

'''if home_screen == ('agc'): #Agc stands for average grade calculation.
	agc = True #Intializes agc and gives a variable for the while loop to work with.
	grade_list = [] #Makes the grade list.
	sum = 0 #This is the sum of all items in the grade list.
	while agc == True: 
		wul = input('Would you like to add a grade (y,n): ') # wul(would you like)
		if wul == ('y'):
			add_grade = int(input('add grade: ')) 
			grade_list.append(add_grade) #Adds the grade to the list.
			sum = 0 #Resets the sum back to 0 
			for item in grade_list:  
				sum += (item) #The sum is all the items 
			print('This is the sum', sum)
			average = (round(sum/len(grade_list)))
			print ('average:  ', average)
		if wul == ('n'):
			print ('average: ', average)
			agc = False'''
