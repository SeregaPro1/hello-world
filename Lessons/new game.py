from typing import Dict


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('-----------------------')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input('Enter (A, B, C or D): ')
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print('Correct!')
        return 1
    else:
        print('Wrong!')
        return 0

def display_score(correct_guesses, guesses):
    print('-----------------------')
    print('Resulst')
    print('-----------------------')
    print('Answers: ', end='')
    for i in questions:
        print(questions.get(i), end='')
    print()

    print('Guesses: ', end='')
    for i in guesses:
        print(i, end='')
    print()

    score = int((correct_guesses/len(questions))*100)
    print('Your score is: '+ str(score)+ '%')


def play_againg():

    responsee = input('Do you want to play again?(y/n): ')
    responsee = responsee.upper()

    if responsee == 'Y':
        return 1
    else:
        return 0

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?:": "C",
    "Is the Earth round?: ": "A"
}

options = [['A. Guido van Rossim', 'B. Elon Musk', 'C. Bill Bates', 'D. Mark Zuckerburg'],
           ['A. 1989', 'B. 1991', 'C. 2000', 'D. 2016'],
           ['A. Lonely Island', 'B. Smosh', 'C. Monty Python', 'D. SNL'],
           ['A. True', 'B. False', 'C. sometimes', 'D. Whats Earth?']]

new_game()

while play_againg():
    new_game()

print("Byeeeeee")