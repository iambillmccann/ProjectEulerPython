import time
import utilities
from problems import ProblemFactory

LASTPROBLEM = 1
QUITSTRING  = 'Q'

def get_user_input():
    """ Get user input from the console
    getUserInput is a simple method for reading from the console.
 
    Returns:
        A string that represents the user's input.</returns>
    """

    return check_user_input(input('What problem shall I run? Or type \'Q\' to quit. '))

def check_user_input(user_input):
    """ Validate the user's input

    checkUserInput will validate the user's input. This is a very redimentary
    validation method. It checks three things ...
    1. Checks for the letter 'Q'
    2. Checks for an integer
    3. Checks that the integer is positive
    4. Checks that the integer is no greater than the last problem solved.
    These checks assume that problems are solved in order.
    Note: If the user enters 'Q', a minus one is returned to the caller.
    
    Args:
        userInput: A string entered by the user.
    
    Returns:
        A valid integer result.
    """

    result = -1
    if user_input.upper() == QUITSTRING: result =  -1
    else:
        try:
            result = int(user_input)
            if result < 1:
                print('\nBTW, problem numbers are positive integers.')
                result = get_user_input()
            elif result > LASTPROBLEM:
                print('\nI have only completed problems 1 through {}'.format(LASTPROBLEM))
                result = get_user_input()
        except ValueError:
            print('\nSorry but I did not understand that. Please type the problem number or Q to quit.')
            result = get_user_input()

    return result

#
# Main Program
#

problem_number = get_user_input()
while (problem_number > 0):
    print('problem number is {}'.format(problem_number))
    solution = ProblemFactory.get_solution(problem_number)

    start_time = time.time()
    result = solution.compute()
    stop_time = time.time()
    total_time = stop_time - start_time

    print('\n-----------------------------------------------------------------------')
    print('Solution to problem {} = {}'.format(problem_number, result))
    print('Execution time was ' + utilities.format_milliseconds(total_time))
    print('-----------------------------------------------------------------------')
    print()

    problem_number = get_user_input()
