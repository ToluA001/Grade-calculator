# This is a very basic pogram that ask the user what type of grade they would like to input and only has one option, individual grade calc. or test calc.

#
from audioop import add


def test_calc():
	if total_ques >= missed_ques:
		ques_right = total_ques - missed_ques #The total num of question - missed question. This gives you the number of right answers and makes calculation easier. 
		raw_score = ques_right / total_ques #Num of questions right divided by total questions gives a grade. 
		user_grade2 = raw_score *100 #This gives the grade as a percent. The user is more likely to recognize the grade this way.
		user_grade2 = round(user_grade2)
		print(user_grade2)
		

home_screen = input('What would you like to do?(igc)(agc) ')
if home_screen == ('igc'): #Stands for individual grade calculator but is more like a test calculator.
	total_ques = int(input('Total questions: '))
	missed_ques = int(input('How many do you think you got wrong: '))
	test_calc()

if home_screen == ('agc'): #agc stands for average grade calculation
	grade_list = []
	sum = 0
	agc = True
	num_of_grade = 0
	while agc == True:
		wul = input('Would you like to add a grade (y,l): ')
		if wul == ('y'):
			add_grade = int(input('add grade: '))
			num_of_grade += 1
			grade_list.append(add_grade)
			for item in grade_list: 
				sum += int(item)
				#print(sum)
				average = sum/len(grade_list)
				print ('average:  ', average)
		if wul == ('l'):
			print (average)
			agc = False

#		if wul ('l'):
#			agc = False


#	for item in grade_list:
#		sum += int(item)
#	print(sum)
#	average = sum/len(grade_list)	
		

'''
if home_screen == ('igc'):
	total_ques = int(input('total questions: '))
	missed_ques = int(input('how many do you think you got wrong: '))
	if total_ques >= missed_ques:
		user_grade = total_ques - missed_ques
		user_grade1 = user_grade / total_ques
		user_grade2 = user_grade1 *100
		print (user_grade2) 
'''
