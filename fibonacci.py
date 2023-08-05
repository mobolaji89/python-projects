"""Fibonacci Sequence
Calculates numbers of the Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
"""

import sys

print ('''The Fibonacci sequence starts with numbers 0 and 1. The next number in the sequence is equal to the sum of the two numbers before it. The Fibonacci numbers list is infinite.''')

while True: # Main program loop
    while True: # Continue asking user for input until user input is valid.
        print('Enter the nth Fibonacci number you wish to')
        print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
        response = input('> ').upper() # make sure user input is forced uppercase to check

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit() # exit program if users enters 'QUIT'

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break  # Exit the loop when the user enteres a valid number.

        print('Please enter a number greater than 0, or QUIT.')
    print() # print blank line

    # Handle the special cases if the user entered 1 or 2:
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
        continue

    # Display warning if the user entered a large number:
    if nth >= 10000:
        print('WARNING: This will take a while to display on the')
        print('screen. If you want to quit this program before it is')
        print('done, press Ctrl-C.')
        input('Press Enter to begin...')

    # Calculate the nth Fibonacci number:
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0, 1, ', end='')  # Display the first two Fibonacci numbers.

    # Display all the later numbers of the Fibonacci sequence:
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1

        # Display the next number in the sequence:
        print(nextNumber, end='')

        # Check if we've found the nth number the user wants:
        if fibNumbersCalculated == nth:
            print()
            print()
            print('The #', fibNumbersCalculated, ' Fibonacci ',
                  'number is ', nextNumber, sep='')
            break

        # Print a comma in between the sequence numbers:
        print(', ', end='')

        # Shift the last two numbers:
        secondToLastNumber = lastNumber
        lastNumber = nextNumber