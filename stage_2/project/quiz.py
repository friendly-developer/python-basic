# IPND Stage 2 Final Project

# All variables that are used across the application

quiz_level_option = ['Easy','Medium','Hard']

intro_statement = 'Hi! Welcome to IPND Python Quiz.'
intro_quiz_options = ", ".join(quiz_level_option)

prob_statement_medium = '''A common first thing to do in a language is display
'Hello ___1___!'  In ___2___ this is particularly easy; all you have to do
is type in:
___3___ "Hello ___1___!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the ___3___ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an ___4___ file in a browser, but it's
a step in learning ___2___ syntax, and that's really its purpose.'''

prob_statement_hard = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

prob_statement_easy = '''Automation in coding programs is a key objective of programming.
Automating not only saves the programmer a lot of time but it is also more efficient programming to automate a program.
An example of automation is using conditional statements.  Python uses many operators but ___1___ operators compare statements and check if value is true or false.
The ___1___ operator ___2___ returns True when the expressions on both sides of ___2___ are True.
The ___1___ operator ___3___ returns True when at least one expression on either side of ___3___ is True.
The ___1___ operator ___4___ returns True for False statements and False for True statements.'''

#options particular to each level
medium_answers = ['World','Python','print','HTML']
hard_answers = ['function','arguments','None','list']
easy_answers = ['boolean','and','or','not']

# input none
# output string
# Displaying error messages that are applicable if invalid input, and take input from user
def get_difficulty_input_user():
    print 'Please select a difficluty level by typing it in!'
    user_input = ''
    max_attempts = 4
    while(user_input.lower() not in ['easy','medium','hard']):
        max_attempts -= 1
        if max_attempts > 0:
            user_input = raw_input('Avaialable options are '+intro_quiz_options+'. ')
        else:
            print "Let us begin with something basic"
            user_input = 'easy'
    return user_input

# input input_option - string
# output string
# Depending on the user difficulty level generate the problem statement
def generate_prob_statements_and_answers(input_option, limit):
    last_level = False
    quiz_index = ['easy', 'medium','hard'].index(input_option.lower())
    if(quiz_index < 2):
        last_level = True
    prob_level = [prob_statement_easy, prob_statement_medium, prob_statement_hard][quiz_index]
    prob_solutions = [easy_answers, medium_answers, hard_answers][quiz_index]
    final_statement = iterate_through_options(prob_solutions, prob_level, limit)
    return final_statement,last_level


# input none
# user input no of chances
# output 
# Ask the user to provide how many number of chances would be needed
def get_chances_input_user():
    input_msg = 'Please provide the number of chances would like to have. Range of options include 1-5 : '
    error_input = 'Invalid option. Lets try again. Please select option between 1-5 : '
    chances_input = raw_input(input_msg)
    while not(chances_input in ['1','2','3','4','5']):
        chances_input= raw_input(error_input)
    return int(chances_input)

# input final_statement - string, last_level - boolean
# output
# Generate messages for user to determine what has happened finally whether he won or not
def play(quiz_level_input,wrong_answers_limit,user_name):
    final_statement,last_level = generate_prob_statements_and_answers(quiz_level_input, wrong_answers_limit)
    print final_statement
    if (final_statement is not None and final_statement != ''):
        print
        print('You Genious. Great Work')
        print 'The correct statement is :'
        print final_statement
        print 'Hey '+user_name+'! Congrats once again. We can always start over!'
        if (not last_level):
            print"Since you have already established you are good. Why don't you try a tougher level?"        
    else:
        print 'Better luck next time '+user_name+'!'
    return ''
    

# input options - list, statement - string, limit - int
# output statement - string
# checking if user input is correct response, if not and displaying the same
def iterate_through_options(options,statement,limit):
    error_option = 0
    index = 1
    while ('___'+str(index)+'___' in statement):
        print statement
        option_select = raw_input('What should be substituted in for ___'+str(index)+'___?')
        if(option_select.lower() == options[index-1].lower()):
            statement = statement.replace('___'+str(index)+'___',options[index-1])
            index = index + 1
        else:
            print error_option
            if (error_option > limit or (error_option == 1 and limit == 1)):
                print 'You have crossed your self defined limit to answer incorrect options!'                
                return ''
            elif ((error_option > (limit-1)) or limit == 1):
                print "This is your last chance. Let's make it count"
            else:
                print 'Incorrect option! Please try again'
            error_option +=1
        print
    return statement

# The main function to execute when the application loads
def start_ipnd_quiz():
    # Greet the user and obtain the difficulty level of the quizz the user wants to try
    print intro_statement
    user_name = raw_input('Before we begin, please let me know what I should call you : ')
    quiz_level_input = ''
    wrong_answers_limit = 0
    quiz_level_input = get_difficulty_input_user()
    if quiz_level_input is None:
        return 'Something went wrong! Let us try again'
    wrong_answers_limit = get_chances_input_user()
    print
    # start quiz process
    play(quiz_level_input,wrong_answers_limit,user_name)
    return ''

print start_ipnd_quiz()

'''https://gist.github.com/anonymous/8401883c0ead6cc7cf6d
I refered my hard statement from here ^
I have tried my best for a responsive UI.
It would be great if you let me know if there are any sort of performance tweaks that
can be done for a better app
'''
