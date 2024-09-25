import random

# the .randomrange() function generates a
# random number within the specified range.
num = random.randrange(1000, 10000)

n = int(input("Four Digit Number: "))

# condition to test equality of the
# number. Program terminates if True.

if (n == num):
    print("Authentification Code Successful")
else:
    # ctr variable initialized. It will keep count of
    # the number of tries made
    ctr = 0

# while loop repeates as long as the
# entry fails

    while n != num:
        # increaments 'ctr'
        ctr += 1

        count = 0

        # explicit type conversion of string to an int
        num = str(num)

        # cprrect[] list stores digits which are correct
        correct = ["X"] * 4

        # for loop runs 4 times since pin has four digits
        for i in range(0,4):

            # checking for equality of digits
            if(n[i]) == num[i]:
                #number of digits guessed correltly increments
                count += 1
                # hence, the digit is stored in correct
                correct[i] = num[i]
            else:
                continue

        # when not all the digits are guessed correctly.
        # if (count < 4) and (count != 0) : this is not needed
        print(f"Not correct. But you did get {count} digits correct.")
        print("These are the numbers which were correct: ")
        for k in correct:
            print(k, end=" ")
        print('\n')
        print("\n")
        n = int(input("Enter the next choice of numbers: "))

elif (count == 0):





