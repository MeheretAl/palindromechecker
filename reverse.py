import time

print("Welcome\n")
while True:
    string = input("The word you want to check please\n")
    reversedstring = string[::-1]
    if reversedstring == string:
        print("Processing ...")
        time.sleep(0.5)
        print(reversedstring)
        print('This word "{}" is a palindrome.'.format(string))
        print("Do you want to check another word?")
    else:
        print("Processing ...")
        time.sleep(0.5)
        print('This word "{}" is not a palindrome.\n'.format(string))
        print("Do you want to check another word?")
    answer = input("Y for Yes and N for No.\n")
    answer = answer.upper()
    if answer == "Y":
        pass
    else:
        break
