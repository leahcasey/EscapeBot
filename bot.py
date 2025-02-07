import random

class EscapeBot:
    
    def __init__(self, name):
        '''the robot name is a parameter than can be changed in different instances, to allow for more flexibility'''
        self.name = name
        self.position = 1
        self.goodbye = "\n\nThank you for playing EscapeBot"
        # lives could be made a parameter and therefore be changed in another version of the game in the future
        # but in this game we want to keep it at 3 lives so there is a base set of lives that can be changed
        self.lives = 3
        self.correct= "\n\n\n\nThat answer was correct! Well done\n"
        self.incorrect= "\n\n\n\nThat answer was incorrect!\n"
        self.win = 'You won!!! \n'
        # this is here cuz im using the set_questions function to reset the questions to the all_dictionary_questions dictionary in main
        self.questions={}

    def __str__(self):
        '''this is a method that displays a string representation'''
        intro="\nBot name: "+self.name
        return intro

    def draw(self, display:'1'): 
        '''this is my robot, they are a cat'''
        # i only have one version of this robot currently, but in the future could make another 
        # which would be displayed for example if 2 was entered as a parameter
        if display=='1':
            print('\n==/\==/\==\n====||====\n==\____/==\n')
        else:
            return ''

    def display_name(self):
        '''in this method the robot introduces themselves to the player'''
        print("Hello! My name is " + self.name + " the EscapeBot!\n\n")

    def instructions(self):
        '''these are the instructions for the escape room game.
        I kept these hardcoded because the instructions are specific to this game'''
        print("I am on a mission.\nI must retrieve the key to open this safe in front of me!\nBut only you can help me...\nYou must help me get the answers to these questions correct before I run out of lives.\nOnly then will I be able to retrieve the key to open the safe!\n ")

    def current_question(self):
        '''this method is used to display the questions, stimulus and possible answers to the player'''
        question = self.questions[self.position]["question"]
        # self.position is the key so it displays the corresponding question, depending on what position the player is at
        stim = self.questions[self.position]["stimulus"]
        ans= self.questions[self.position]["answers"]
        ans2=list(ans)
        random.shuffle(ans2)
        # this randomly shuffles the possible answers without changing the origional list in the dictionary
        # as it is assigned to another variable
        print('Question ', self.position , '\n' , question , '\n -->  ' , stim , '\n\nPossible answers are:\n' , ans2)

    def check_answer(self, response):
        '''this method chgecks if the response given is the correct answer or incorrect'''
        response=str(response)
        response=response.lower()
        # this ensures that even is the response if givemn capitalised, the function will still understand it
        response.strip()
        # this eliminates extra spaces before and after the word
        ans=str(self.questions[self.position]["answers"][0])

        if response==ans.lower():
            # if the response given is the same as the correct answer in the dictionary
            return True
        else:
            # if the response was incorrect
            return False

    def reset(self):
        '''this method resets the players position to position 1'''
        self.position==1

    def display_lives(self):
        '''this method displays how many lives the player has left'''
        print("You have",self.lives, "lives remaining...\n")

    def life_gained(self):
        '''this function is the last feature i added to this project. it is only called if the user only has one life left, and answers the next question correctly'''
        # lets the user know they have gained a life
        print('You have now gained a life!!!\n')
        # lives are incremented by 1
        self.lives+=1
        # it also displays the new amount of lives to the user(which is 2)
        self.display_lives()

    def decrement_lives(self):
        '''this method takes away one of the players lives, and is used when the player answers incorrectly'''
        self.lives-=1
        if self.lives>0:
            # if the player still has lives left, the game continues
            return True
        if self.lives==0:
            # if the player runs out of lives, they lose
            print ('Game over! You failed to help me retrieve the key to open this safe. you lost, loser!\n')
            return False

    def increment_position(self):
        '''this method increments the players position'''
        self.position = self.position + 1
        # i changed this from the hardcoded 5 to len(self.questions) so that it accounts for more or less questions
        if self.position > len(self.questions):
            # if position is greater than the amount of questions, then the player has played all questions
            self.position = self.position - 1
            return True
        else:
            return False

    def reveal_answer(self):
        '''this method reveals the correct answer to the player, but is only used once the player has lost the game'''
        correct_answer = self.questions[self.position]["answers"][0]
        print("The correct answer was: %s\n" % correct_answer)
    
    def set_questions(self, new_questions):
        '''this method allows for a new set of questions to be used in the game'''

        if type(new_questions) != dict:
            print("Questions must be of type dictionary (nested). Questions not reset.\n")
            return

        for key in new_questions:
            if str(key).isdigit() == False:
                print("Questions are not in the correct format. Questions not reset")
                return
            else:
                keys = new_questions[key]
                if type(keys) != dict:
                    print("Questions must be of type dictionary (nested). Questions not reset.")
                    return
                if len(keys) != 3:
                    print("Questions are not in the correct format. Questions not reset")
                    return -1
                if "question" not in keys and "answers" not in keys and "stimulus" not in keys:
                    print("Questions are not in the correct format. Questions not reset")
                    return
        print("questions reset!")    
        self.questions = new_questions

            

    def get_botname(self):
        return self.name
    
    def set_botname(self, new_name):
        self.name=new_name
    
    property=(get_botname,set_botname)

    def finished_game(self):
        '''this method return a message after the player has played all 5 questions'''
        print("All questions have now been played!\n")

    def terminate_message(self):
        '''this method thanks the player for playing EscapeBot'''
        print(self.goodbye)
    
    def terminate(self):
        '''this method displays the final game termination message'''
        print('this game has now been terminated')

    def display_position(self):
        '''this method displays the players position to them'''
        print("you are at position %s " % self.position + '\n')
