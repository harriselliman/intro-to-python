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

