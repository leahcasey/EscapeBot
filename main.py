from filereader import *
from bot import *

# file_reader1=FileReader("python-game-file.txt")
qfr=QuestionFileReader("python-game-file.txt")
# print(qfr.all_dictionary_questions())
# print(qfr.get_dictionary_range([3,6]))
# print(qfr.get_dictionary_range([0,1]))
# print(qfr.get_dictionary_range([6,7]))
# print(qfr.lines_as_dictionary([1,3,5]))
# print(qfr.random_dictionary_questions())
# print(qfr.exclude_dictionary_questions([1,3,5,7]))
# print(qfr.exclude_dictionary_range([1,6]))
# ------- main code section

# # this is my instance of escapebot
escape_bot = EscapeBot('Daisy')
escape_bot.set_questions(qfr.all_dictionary_questions())


# this prints the string representation of the bots name
print(escape_bot)
# this displays the robot
escape_bot.draw('1')
# the robot introduces themselves
escape_bot.display_name()
# the robot gives the player instructions
escape_bot.instructions()

in_play = False

user_in = input("Press Y to continue. Any other key quits the game!")
# if the player decides to play the game, in_play is true and the game begins
if user_in.lower() == "y":
    print('\n'*10)
    in_play = True
else:
    # the game does not play, and is terminated
    print('\n'*10)
    in_play = False

while in_play:
    # firstly, the players position is displayed
    escape_bot.display_position()
    # then the current question is displayed
    escape_bot.current_question()
    # and the player is prompted for their answer
    response = input('\n\nWhat is your guess? Type the full answer:')

    
    if escape_bot.check_answer(response)==True:
        # if the player responds correctly
        print(escape_bot.correct)
        # if the player answers correctly, it automatically moves on to the next question
        user_in = 'y'
        #  if the player only has one life left, and they just answered a question correctly
        if escape_bot.lives==1:
            # then they will gain a life, even if it is the last question in said game
            escape_bot.life_gained()

    if escape_bot.check_answer(response)==False:
        # if the player answers incorrectly
        # print('\n'+escape_bot.incorrect)
        print(escape_bot.incorrect)
        # takes away a life
        escape_bot.decrement_lives()
        # shows the player have many lives they now have left
        escape_bot.display_lives()

        if escape_bot.lives>1:
            # this makes is so that if the player answers incorrectly but still has lives left, the remain at the same question
            user_in = "n"

        if escape_bot.lives==1:
            # this makes is so that if the player answers incorrectly but still has lives left, the remain at the same question
            print('You now have one life remaining. If you get the next question correct, you will gain a life! \nIf you get it wrong YOU LOSE. last chance.....\n')
            user_in = "n"
        
        if escape_bot.lives==0:
            # if the player has no lives left
            # reveals the correct answer to the player
            escape_bot.reveal_answer()
            # this message only shows if players have actually played the game (rather than quitting before seeing first question)
            escape_bot.terminate_message()
            in_play = False

    if user_in.lower() == "n":
        # if the player gets the answer wrong, this lets the code continue and redisplays the same question 
        continue

    if user_in.lower() == "y":
        # every time the answer a question correctly, and they choose to move on, their position is incremented
        no_questions_left = escape_bot.increment_position()
        # this increments the users position
        if no_questions_left == True:
            # this checks if the uses has answered all questions, and finishes the game when they do
            escape_bot.finished_game()
            # the player has won the game if they answered all questions, and haven't lost all their lives
                         # this message only shows if players have actually played the game (rather than quitting before seeing first question)
            print(escape_bot.win)
            escape_bot.draw('1')
            # only once the player has won this game, this asks the player if they would like to start a new game with a set of new questions
    
            possible_newgame=input('Would you like to play a new game with a new set of questions? \nPress Y for yes, or press any other key quits the game! ')
            # if the users answers YES that they would like a new game with new questions
            if possible_newgame.lower()=='y':
                # newf is the user input, which will be passed as a parameter into the change_dict_questions method
                newf=input('\n\nPlease enter the name of the file you would like to use.\nIf the file does not exist, the same questions from the last game will replay: ')
                # this is a good example of object interaction between the two classes
                escape_bot.set_questions(qfr.change_dict_questions(newf))
                # user position and lives are reset for the new game
                escape_bot.position=1
                escape_bot.lives=3               

            else:
                # if the user does not want to play another game with new questions, the game terminates
                escape_bot.terminate_message()
                in_play = False

    
# once the game is over
escape_bot.draw('1')
# robot returns before game is terminated
escape_bot.terminate()
# player position is reset to 1
escape_bot.reset()




# i know we didnt change anything in the parent class, but i added these tests for it just incase you wanted them haha
# print(file_reader1.read_all())
# print(file_reader1.line_count())
# print(file_reader1.get_filename())
# print(file_reader1.set_filename())

# print(qfr.__str__())

# print(qfr.all_dictionary_questions())

# in these next two methods, they each take one parameter that must be a list
# print(qfr.lines_as_dictionary([1,3,5]))

# this one must be a list with only 2 ints
# print(qfr.get_dictionary_range([1,3]))

# print(qfr.random_dictionary_questions())


# these next two methods also they each take one parameter that must be a list
# print(qfr.exclude_dictionary_questions([4,5,6,7]))

# print(qfr.exclude_dictionary_range([3,4]))
