# This is a very basic pogram that ask the user what type of grade they would like to input and only has one option, 
# individual grade calc. or test calc.
import datetime
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
		if add_tg >=  0 and add_tg <= 100: # Makes sure the user can only input grades 0 - 100
			tg_list.append(add_tg) # Adds the grade to the test grade list. 
			print ('added', tg_list, 'test grades') # This is temporary and will not be in the final product, prints list.
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
		if add_dg >= 0 and add_dg <= 100:
			dg_list.append(add_dg)
			print ('added', dg_list, 'daily grades')
		if add_dg > 100 or add_dg < 0:
			print ('number inputted not valid')
		
def daily_average():
	dg_sum = 0
	for x in dg_list:
		dg_sum += (x)

	dg_average = dg_sum / len(dg_list)

	return dg_average

def average(): # Function for the total average.
	t_sum = 0 # Initailize total sum to 0.
	d_sum = 0
	for x in tg_list: # Gets the sum of both lists. 
		t_sum += ((x)*.55)
	
	for grade in dg_list:
		d_sum += ((grade)*.45)
	
	dg_ave = d_sum /len(dg_list)# gets the average 
	tg_ave = t_sum /len(tg_list)

	# If the length of both list is greater or equal to 2 it runs this if.
	total_ave = round(dg_ave + tg_ave) # The Addition of 

	if total_ave <= 59: # Gives letter grade based on if the average is in a certain range of numbers.
		print("Letter grade: F")
	if total_ave <= 62 and total_ave >= 60:
		print("Letter grade: D-")
	if total_ave <= 66 and total_ave >= 63:
		print("Letter grade: D")
	if total_ave <= 69 and total_ave >= 67:
		print("Letter grade: D+")
	if total_ave <= 72 and total_ave >= 70:
		print("Letter grade: C-")
	if total_ave <= 76 and total_ave >= 73:
		print("Letter grade: C")
	if total_ave <= 79 and total_ave >= 77:
		print("Letter grade: C+")
	if total_ave <= 82 and total_ave >= 80:
		print("Letter grade: B-")
	if total_ave <= 86 and total_ave >= 83:
		print("Letter grade: B")
	if total_ave <= 89 and total_ave >= 87:
		print("Letter grade: B+")
	if total_ave <= 92 and total_ave >= 90:
		print("Letter grade: A-")
	if total_ave <= 96 and total_ave >= 93:
		print("Letter grade: A")
	if total_ave <= 100 and total_ave >= 97:
		print("Letter grade: A+")
	# Theres definatly a better way I could do that. 
	return total_ave

'''	if len(tg_list) <= 1 and len(dg_list) <= 1:
		raw_s = (dg_ave + tg_ave)
		return raw_s

	#raw_s = t_sum + d_sum / len(tg_list)
	if len(tg_list) >= 2 and len(dg_list) <= 1:
		raw_s = dg_ave + tg_ave
		ave1 = raw_s / len(tg_list)
		ave2 = ave1 / len(dg_list)
		return ave2'''

def home_screen(): # This is the function that starts the pogram. 
	print ('Igc stands for individual grade calculator.')
	print ('Agc stands for average grade calculator.')
	print ("Press 'a' when prompted to get the average.")
	global screen 
	screen = input('What would you like to do?(igc)(agc)(quit) ')

home_screen() # This is calling function that starts the pogram.

while screen != ('quit'):
	if screen == ('igc'): #Stands for individual grade calculator but is more like a test calculator.
		total_ques = int(input('Total questions: '))
		missed_ques = int(input('How many do you think you got wrong: '))
		test_calc()
		home_screen()


	if screen == ('agc'): #Agc stands for average grade calculation.
		agc = True #Intializes agc and gives a variable for the while loop to work with.
		tg_list = [] # Test grade list. 
		dg_list = [] # Daily grade list
		while agc == True: # 
			add_grade = input('Would you like to add a grade(y,n): ') # Asks the user if they would like to add a grade.
			if add_grade == ('y'):
				t_d = input('Is a daily or test grade(d,t): ')


				while t_d == ('d'):
					daily() # Calls the daily grade function if the user inputs d. 
					add_grade = input('Would you like to add a grade(y,n,a): ')
					t_d = input('Is it a daily or test grade(d,t,a): ')

				while t_d == ('t'):
					test() # Calls the test grade function if the user unputs t. 
					add_grade = input('Would you like to add a grade(y,n,a): ')
					t_d = input('Is it a daily or test grade(d,t,a): ')

			
			if add_grade == ('a'): 
				# if add grade is no the user may get the average and restart the program
				avg = input('get average(y,n)? ')
				if avg == ('y'):
					print('test average: ', test_average())
					print('daily average: ', daily_average())
					print('your average is: ', average())
					agc = False
					home_screen()
				else:
					agc = False
					home_screen()


