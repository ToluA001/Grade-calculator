
# This is a very basic pogram that ask the user what type of grade they would like to input and only has one option, individual grade calc. or test calc.


home_screen = input('What would you like to do? ')


if home_screen == ('igc'):
	total_ques = int(input('total questions: '))
	missed_ques = int(input('how many do you think you got wrong: '))
	if total_ques >= missed_ques:
		ques_right = total_ques - missed_ques #The total num of question - missed question. This gives you the number of right answers and makes calculation easier. 
		raw_score = ques_right / total_ques #Num of questions right divided by total questions gives a grade. 
		user_grade2 = raw_score *100 #This gives the grade as a percent. The user is more likely to recognize the grade this way.
		print (user_grade2) 

