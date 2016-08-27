# IPND Stage 2 Final Project

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''


# All variables that are used in the function
quiz_level_option = ['Easy','Medium','Hard']
intro_statement = 'Hi! Welcome to IPND Python Quiz. Please select one of the below options'
intro_quiz_options = "/".join(quiz_level_option)

prob_statement1 = 'Problem statement 1'
prob_statement2 = 'Problem statement 2'
prob_statement3 = 'Problem statement 3'


# Greet the user and obtain the difficulty level of the quizz the user wants to try
# Depending on the user difficulty level generate the problem statement
# Ask the user to provide how many number of chances would be needed
# Show the problem statement and ask the user to provide an input
# each problem statement will have its predefined options mapped to it
# checking if user input is correct response
# bidding good bye to the user

# The main function to execute when the application loads
def start_ipnd_quiz():
    print intro_statement
    print intro_quiz_options
    return ''

print start_ipnd_quiz()
