import random

#The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston','Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre',
'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#create 35 text file of questions and answers
#for each of the 35 text file of questions and answers create 50 questions and their solutions

for i in range(35):
    QuestionfileObj = open(f'capitalQuestions{i+1}','w')
    QuestionfileObj.write(f"{' ' * 20} CapitalQuiz{i+1}\n\n")
    QuestionfileObj.write('Name: \n')
    QuestionfileObj.write('Date: \n')
    QuestionfileObj.write('\n\n')

    AnswerfileObj = open(f'capitalAnswers{i+1}','w')
    AnswerfileObj.write(f"{' ' * 20} CapitalAnswers{i+1}\n\n")
    state = list(capitals.keys())
    random.shuffle(state)
    for QuestionNumber in range(50):
        CapitalInQuestion = state[QuestionNumber]
        correctAnswer = capitals[CapitalInQuestion]
        wrongAnswer_list = list(capitals.values())
        del wrongAnswer_list[wrongAnswer_list.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer_list,3)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)
        QuestionfileObj.write(f"{QuestionNumber + 1}. What is the capital of {CapitalInQuestion}?\n")
        for i in range(4):
            QuestionfileObj.write(f"{'ABCD'[i]}. {answerOptions[i]}\n")
        QuestionfileObj.write(f"\n\n")
        correctAnswerOption = answerOptions.index(correctAnswer)
        AnswerfileObj.write(f"{QuestionNumber + 1}.{'ABCD'[correctAnswerOption]}\n")
    QuestionfileObj.close()
    AnswerfileObj.close()


print('Job Done')