# basic calculator

'''num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter another number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")'''


# basic guessing game

'''secret_word = "elephant"
guess = ""
guess_count = 1
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count <= guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose.")
else:
    print("Correct, the secret word is " + secret_word)'''



# build a basic translator

'''def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "V"
            else:
                translation = translation + "v"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))'''


# reading files

'''player_file = open("/Users/harriselliman/Desktop/CODE./PYTHON./intro-to-python/players.txt", "r")

print(player_file.readable())
print(player_file.read())
print(player_file.readline())
print(player_file.readlines())

for player in player_file.readlines():
    print(player)

player_file.close()'''

# ammend files

'''player_file = open("/Users/harriselliman/Desktop/CODE./PYTHON./intro-to-python/players.txt", "a")

player_file.write("\nSadio Mane - Left Winger")
player_file.write("\nFabinho - Defensive Midfielder")

player_file.close()'''

# writing files

'''player_file = open("/Users/harriselliman/Desktop/CODE./PYTHON./intro-to-python/players.txt", "w")

player_file.write("Alisson Becker - Goalkeeper")

player_file.close()'''

'''html_file = open("/Users/harriselliman/Desktop/CODE./PYTHON./intro-to-python/index.html", "w")

html_file.write("<p>This is a HTML file</p>")

html_file.close()'''

# modules

'''import useful_tools

print(useful_tools.roll_dice(6))'''


# classes & objects

'''from Student import Student

student1 = Student("Jack", "Economics", 4.0, False)
student2 = Student("Kevin", "Software Engineering", "1.2", True)

print(student1.name)
print(student2.gpa)'''

# basic multiple choice quiz

from Question import Question

question_prompts = [
    "What colour are Oranges?\n(a) Green\n(b) Orange\n(c) White \n\nAnswer: ",
    "What colour kit do Liverpool wear?\n(a) Red\n(b) Blue\n(c) Brown\n\nAnswer: ",
    "What colour is the sky?\n(a) Yellow\n(b) Purple\n(c) Blue\n\nAnswer: "
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")