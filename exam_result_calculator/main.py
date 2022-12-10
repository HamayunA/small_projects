import sys

number_of_questions = int(input("How many questions are on the test? "))

choices = 0
while choices <= 1: 
    choices = int(input("How many choices per question? "))

certain = int(input("How many questions are you certain that you got right? "))
guessed = int(input("How many questions did you guess? "))

if certain + guessed != number_of_questions:
    sys.exit("The number of questions you're certain of and the ones you guessed don't add up to the number of questions on the whole test. Maybe A typo?")

certain_percentage = certain/number_of_questions*100
guessed_percentage = guessed/number_of_questions*100*1/choices

print(f"You probably got around {round(certain_percentage + guessed_percentage)}% on your test. :)")



