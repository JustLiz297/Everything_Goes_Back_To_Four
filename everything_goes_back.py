def translate(number):
    if (number > 15 or number < 0):
        return 'error'
    elif number == 0:
        return 'zero'
    elif number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
    elif number == 4:
        return 'four'
    elif number == 5:
        return 'five'
    elif number == 6:
        return 'six'
    elif number == 7:
        return 'seven'
    elif number == 8:
        return 'eight'
    elif number == 9:
        return 'nine'
    elif number == 10:
        return 'ten'
    elif number == 11:
        return 'eleven'
    elif number == 12:
        return 'twelve'
    elif number == 13:
        return 'thirteen'
    elif number == 14:
        return 'fourteen'
    elif number == 15:
        return 'fifteen'


playing = True
print("Welcome to the Everything Goes Back to Four! Would you like to play?")
line = 'Y/N: '
correct = False
answer = '_'
user_input = input(line)
if user_input == 'n':

    playing = False
else:
    while playing == True:
        correct = False
        print("----------------------------")
        print("Enter a number (Between 0 & 15): ")
        answer = input()
        answer = translate(int(answer))
        while answer == 'error':
            answer = input("That is not a valid number, try again: ")
            answer = translate(int(answer))
        length = 0
        while length != 5 and answer != 'five' and answer != 'nine' and answer != 'four':
            length = len(answer)
            print(answer.capitalize() + " goes to " + str(length))
            answer = translate(length)
            
        print("And " + answer + " goes to 4, so everything goes back to four.")
        print("Do you now know why everything goes back to four?")
        answer = input(line)
        if answer.lower() == 'y':
            print("What is the trick?")
            user_input = input()
            if user_input.lower() == 'word length':
                print("Correct!")
            else:
                print("Nope, not quite.")
        print("Would you like start again?")
        user_input = input(line)
        if user_input.lower() == 'n':
            playing = False

print("Goodbye!")
