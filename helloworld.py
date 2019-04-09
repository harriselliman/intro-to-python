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

def translate(phrase):
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


print(translate(input("Enter a phrase: ")))