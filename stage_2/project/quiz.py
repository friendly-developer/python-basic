# IPND Stage 2 Final Project

# All variables that are used across the application

quiz_level_option = ['Easy','Medium','Hard']

intro_statement = 'Hi! Welcome to IPND Python Quiz.'
intro_quiz_options = ", ".join(quiz_level_option)

prob_statement_easy = '''A common first thing to do in a language is display
'Hello ___1___!'  In ___2___ this is particularly easy; all you have to do
is type in:
___3___ "Hello ___1___!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the ___3___ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an ___4___ file in a browser, but it's
a step in learning ___2___ syntax, and that's really its purpose.'''

prob_statement_medium = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

prob_statement_hard = '''Automation in coding programs is a key objective of programming.  
               Automating not only saves the programmer a lot of time but it is also more efficient programming to automate a program.  
               An example of automation is using conditional statements.  Python uses many operators but __1__ operators compare statements and check if value is true or false.  
               The __1__ operator __2__ returns True when the expressions on both sides of __2__ are True.   
               The __1__ operator __3__ returns True when at least one expression on either side of __3__ is True.  
               The __1__ operator __4__ returns True for False statements and False for True statements.'''

#options particular to each level
easy = ['World','Python','print','HTML']
medium = ['function','arguments','None','list']
hard = ['boolean','and','or','not']


# Displaying error messages that are applicable if invalid input, and take input from user
def get_difficulty_input_user():
    print 'Please select a game difficulty by typing it in!'
    valid_input = ''
    invalid_times = 0
    invalid_input = True
    max_attempts = 4
    while(invalid_input):
        if invalid_times > max_attempts:
            print 'You have given five invalid inputs. Please restart the quiz.'
            return
        if invalid_times > max_attempts - 1:
            print 'You have given four invalid inputs. This is your last chance'
        valid_input = raw_input('Avaialable options are '+intro_quiz_options+'. ')
        for option in quiz_level_option:
            if option.lower() == valid_input.lower():
                invalid_input = False
        if invalid_input:
            print('Invalid Option. Please try again')
            invalid_times += 1
    return valid_input    

# Depending on the user difficulty level generate the problem statement
def generate_prob_statements(input_option):
    if(quiz_level_option[0].lower()==input_option.lower()):
        return prob_statement_easy
    if(quiz_level_option[1].lower()==input_option.lower()):
        return prob_statement_medium
    if(quiz_level_option[2].lower()==input_option.lower()):
        return prob_statement_hard
        
    
# Ask the user to provide how many number of chances would be needed
def get_chances_input_user():
    num_of_chances = 0
    input_msg = 'Please provide the number of chances for a wrong answer you would like to have before getting disqualified. Range of options include 1-5 : '
    error_input = 'Invalid option. Lets try again. Please select option between 1-5 : '
    isFirst = True
    chances_input = 0
    while not(chances_input in [1,2,3,4,5]):
        try:
            if(isFirst):
                isFirst = False
                chances_input= int(raw_input(input_msg))
            else:
                chances_input= int(raw_input(error_input))
        except ValueError:
            print("This is not a number")            
    num_of_chances = chances_input
    return num_of_chances

# Show the problem statement and ask the user to provide an input
def display_and_obtain_options(level,limit):
    prob_statement_current = generate_prob_statements(level)    
    return generate_options_and_inputs(level,limit,prob_statement_current)
    
# each problem statement will have its predefined options mapped to it
def generate_options_and_inputs(level,limit,statement):    
    options=[]    
    last_level = False
    print 'The current problem statement reads as below :'
    if(level == quiz_level_option[0].lower()):
        options = easy
    elif(level == quiz_level_option[1].lower()):
        options = medium
    elif (level == quiz_level_option[2].lower()):
        options = hard
        last_level = True
    final_statement = iterate_through_options(options,statement,limit)
    return display_final_messages(final_statement)

# Generate messages for user to determine what has happened finally whether he won or not
def display_final_messages(final_statement):
    if (final_statement is not None ):
        print
        print('You Genious. Great Work')
        print 'The correct statement is :'
        print final_statement
        if (not last_level):
            print"Since you have already established you are good. Why don't you try a tougher level?"
        return 'finish'
    return 

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
            print
            if (error_option > limit or (error_option == 1 and limit == 1)):
                print 'You have crossed your self defined limit to answer incorrect options!'
                print 'This appliccation will exit now. Thanks!'
                return            
            elif (error_option > limit-1 or limit == 1):
                print 'This is your last chance. Please make it count'                
            else:                 
                print 'Incorrect option! Please try again'
            print
            print statement
            error_option +=1
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
        return 
    wrong_answers_limit = get_chances_input_user()
    print 
    # start quiz process   
    finish = display_and_obtain_options(quiz_level_input,wrong_answers_limit)
    print
    print
    if (finish == 'finish'):        
        print 'Hey '+user_name+'! Congrats once again. We can always start over again!'
    else:
        print 'Better luck next time '+user_name+'!'
    return ''

print start_ipnd_quiz()

'''https://gist.github.com/anonymous/8401883c0ead6cc7cf6d
I refered my hard statement from here ^
I have tried my best for a responsive UI. 
It would be great if you let me know if there are any sort of performance tweaks that can be done for a better app
'''
