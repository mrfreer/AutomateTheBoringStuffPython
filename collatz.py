#interesting
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3*number + 1)
        return (3*number+1)

num = 1
while num == 1:
    try:
        userInput = int(input("Enter a number:"))
        while userInput != 1:
            userInput = collatz(userInput)
    except ValueError:
        print('Please enter an integer.')
        continue
    break




