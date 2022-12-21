# This is a very basic pogram that ask the user what type of grade they would like to input and only has one option, individual grade calc. or test calc.


from ast import While
from audioop import add


def test_calc():
	if total_ques >= missed_ques:
		ques_right = total_ques - missed_ques #The total num of question - missed question. This gives you the number of right answers and makes calculation easier. 
		raw_score = ques_right / total_ques #Num of questions right divided by total questions gives a grade. 
		user_grade2 = raw_score *100 #This gives the grade as a percent. The user is more likely to recognize the grade this way.
		user_grade2 = round(user_grade2)
		print(user_grade2)

def test():
	if t_d == ('test'):
		add_tg = int(round(float(input('Add a test grade: '))))
		if add_tg > 0 and add_tg <= 100:
			tg_list.append(add_tg)
			print (tg_list)
		if add_tg > 100 or add_tg < 0:
			print ('number inputed not valid')

 
def test_average():
	tg_sum = 0
	for item in tg_list:
		tg_sum += (item)

	tg_average = tg_sum / len(tg_list)

	return tg_average


def daily():
	if t_d == ('daily'):
		add_dg = int(round(float(input('Add a daily grade: '))))
		if add_dg > 0 and add_dg < 100:
			dg_list.append(add_dg)
			print (dg_list)
		if add_dg > 100 or add_dg < 0:
			print ('number inputted not valid')
		
#def daily_average():


home_screen = input('What would you like to do?(igc)(agc) ')
if home_screen == ('igc'): #Stands for individual grade calculator but is more like a test calculator.
	total_ques = int(input('Total questions: '))
	missed_ques = int(input('How many do you think you got wrong: '))
	test_calc()


if home_screen == ('agc'): #Agc stands for average grade calculation.
	agc = True #Intializes agc and gives a variable for the while loop to work with.
	tg_list = []
	dg_list = []
	while agc == True:
		add_grade = input('Would you ilke to add a grade: ')
		if add_grade == ('y'):
			t_d = input('Is a daily or test grade: ')

		while t_d == ('daily'):
			daily()
			add_grade = input('Would you like to add a grade: ')
			t_d = input('Is it a daily or test grade: ')

		while t_d == ('test'):
			test()
			add_grade = input('Would you like to add a grade: ')
			t_d = input('Is it a daily or test grade: ')

		if add_grade == ('n'):
			avg = input('get average?')
			if avg == ('y'):
				print(test_average())
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
