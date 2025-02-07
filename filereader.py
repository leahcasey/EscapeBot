import random

class FileReader:

    def __init__(self, filename):
        self.__filename = filename
        print("instance of FileReader class created!")
    
    def read_all(self):
        '''this method reads all of the line in the file'''
        try:
            # this opens the file
            file_1 = open(self.__filename)
            # this gets/reads all of the lines in the file
            lines = file_1.readlines()
            # this closes the file
            file_1.close()
            return lines
        except:
            # error handling
            print("file not opened. Terminating method")
            return False

    def line_count(self):
        '''this method counts all of the lines in a file'''
        # it uses the read all method to get all the lines in the file
        lines = self.read_all()
        # it then gets the amount of lines in the file using len()
        line_amount = len(lines)
        return line_amount   

    def get_filename(self):
        # this is a getter for getting the filename. It is needed as the filename is a private instance variable
        return self.__filename
    def set_filename(self, new_filename):
        # this method sets the file name to a new name
        self.__filename = new_filename 

class QuestionFileReader(FileReader):

    def __init__(self, fname):
        '''i created a new __init__ for this file (method overriding)
        as the filename is a private instance variable in the parent class'''
        # i used super( to access the __init__ in the parent class
        # so that we can use it e.g. when using methods from parent class, in this classs
        super().__init__(fname)
        # since the instance of file name in the parent class is private, i use the getter to get the filename
        self.fname=super().get_filename()
    
    def __str__(self):
        '''this is a string representation, explaining what this class does'''
        return 'File name: %s \nThis class contains several methods including converting content from a text file into a nested dictionary' %self.fname

    def change_dict_questions(self, new_file):
        '''this function is called only after the user has won the game, and chooses to play a new game with a new set
        of questions. If the user enters nothing, then our default file (python-game-file.txt) will be used '''
        # using inheritance, this method uses super() toi access the set filename method from the parent class
        # and it uses method overriding to set the new file name, as whatever filename the user inputs
        try:
            # if the file name given is the one that is already being used
            if new_file==self.get_filename():
                # then the game will generate a random range of questions from the dictionary
                #  a good example of efficient code reuse
                return self.random_dictionary_questions()
            # if the 'new file' givcn doesn't even end in txt
            if new_file[::4]!='.txt':
                # then just generate a random range of questions from the dictionary being used
                return self.random_dictionary_questions()
            else:
                # if the new file name given is not the one already being used, and it exists
                super().set_filename(new_file)
                # and generate a dictionary of questions using the file, another good example of efficient code reuse
                return self.all_dictionary_questions()
        except:
            return 'Oops, an error has occured while changing the questions, please enter a valid filename'



    def all_dictionary_questions(self):
        '''This method reads the entire contents from the file specified, 
        aside from line number 0(as we don't need it) This method then converts this content to the nested dictionary format '''
        
        try:
            # this calls the read all method from the parent class and assigns it to a variable
            # sp it gived me all the contents of the file
            b = self.read_all()
            # this gets rid of the first line in the file from the variable
            b.pop(0)
            # this will be the nested dictionary where the keys are numbers
            dict2={}
            # this gives me the amount of lines in the file
            len_file=len(b)
            # here is my counter, which i increment in the while loop
            i=0
            
            while i < len_file:
                # the while loop stops when i has incremented through all lines within the length of the file
                # this will be the dictionary with questions,stimulus and answers
                dict1={}
                ans_list=[]
                # this gives me the line in the file which corresponds to i / at index i
                line=b[i]
                # this gets rid of the unneccessary '\n's in the file content
                # and splits the line by the commas
                new=line.strip('\n').split(',')
                # my first key is 'question', which is at the first index of the line
                dict1['question']=new[0]
                # my second key is 'stimulus', which is at the second index of the line
                dict1['stimulus']=new[1]
                # my new counter called j, the first two indexes in new are the question and 
                # the stimulus, everything after that are the possible answers, this code account for if there are any amount of possible answers
                j=2
                while j < len(new):
                    # append new at index j into the answer list
                    ans_list.append(new[j])
                    j+=1

                # my second key is 'answers', 
                # the value related to the answers key, is the answers list
                dict1['answers']=ans_list
                # increment here as i starts at 0 and we want the first key 
                # of the nested dictionaruy to be 1
                i+=1
                # in the nested dictionary, the outer key will be a number, and the values
                # in it will be the inner dictionary we created
                dict2.update({i:dict1})
                
            # this returns the nested dictionaru
            return dict2

        # error handling, incase the code doesn't work as it should
        except:
            return 'Oops a problem has occured'

    def lines_as_dictionary(self, line_nums_list:list):
        '''this method returns the questions, stimuli and answers in the dictionary 
        format provided above at the line numbers specified in the list passed in (line_nums_list).'''
        
        try:
            # i use this function to get the nested dictionary i created in all_dictionary_questions
            dict_qs = self.all_dictionary_questions()
            # this will be the dictionary thats returned
            ret = {}
            # i starts at 1 as we dont have a question 0
            i=1
            # while i is less than the length of line_nums_list
            while i < len(line_nums_list):
            # for every value in line_nums_list
                for var in line_nums_list:
                    # get the values in the nested dictionary at the key given(var from line_nums_list)
                    var1 = dict_qs.get(var)
                    # update the new dictionary with the var(s) from line_nums_list as a key
                    # and var1 is the content we just retrieved from our nested dictionary created before
                    ret.update({i:var1})
                    # increment i so the questions are in consecutive order e.g. 1,2,3 etc.
                    i+=1
                # return the new dictionary
                return ret
        except:
            return 'Oops a problem has occured'
        

    def get_dictionary_range(self, ran):
        '''this method reads from a range of values (provided in ran) 
        from the file from a given line range. It returns those questions, 
        stimuli and answers in the dictionary format above.'''
        
        try:
            b = self.read_all()
            # this gets rid of the first line in the file from the variable
            b.pop(0)
            # this gives me the amount of lines in the file
            len_file=len(b)
            # check if either value is greater than the amount of lines in the list
            # this if statement ensures this code onbly runs if ran is given inj the correct format
            #  ensuring the list only has 2 items, the first number is smaller than the second, that neither of the numbers are negative, 
            # and also that neither of the numbers are greater than the length of lines in the list
            if len(ran)==2 and ran[0]<ran[1] and ran[0]>0 and ran[1]>0 and ran[0]<len_file and ran[1]<=len_file:
                # ran[0] cannot be 0 as my lines begin at 1
                # i use this function again to get the nested dictionary
                c = self.all_dictionary_questions()
                # this will be the dictionary thats returned
                ret = {}
                # i added 1 to the ending value so that the ending value in the range is 
                # included in the returning dictionary
                end = ran[1]+1
                # for every value in line_nums_list
                i=1
                while i < end:
                    for var in range(ran[0],end):
                        # return the value in the dictionary at the key given
                        var1=c.get(var)
                        # make a new dictionary with the index you want
                        ret.update({i:var1})
                        i+=1
                    return ret
            else:
                return 'Ensure list(ran) is in correct format, that there are no more than 2 values in the list, no negative values given, the second value in the list is greater than the first and also ensure either value is not greater than the amount of lines available in the file.'
        except:
            return 'Oops a problem has occured.'
        

    def random_dictionary_questions(self):
        '''this method reads lines from the file from a random line 
        range (between a start value and a stop value (inclusive of both) '''
        
        try:
            c = self.all_dictionary_questions()
            # this calls a methjod from the parent class to get the amount of lines in the file
            lines=self.line_count()
            # # i minus 1 from lines, and i do not include the first line (index(0) in the file as it is not a question)
            lines=lines-1
            # i get 2 random numbers within the range of how many lines are in the file (in this case its 1-7)
            #  but i used line count so that the code is more flexible and still works if there are more lines in the file
            num1=random.randint(1,lines)
            num2=random.randint(1,lines)
            # my returning dictionary
            ret = {}

            #  if the two numbers are the same
            if num1==num2:
                # then just change one of the numbers using a while loop, so that it keeps looping until the numbers arent the same
                while num1==num2:
                    num1=random.randint(1,lines)

            # if the first number is less than num2, that makes num2 the ending value in the range
            # these if statements ensure that the first number in the range is less than the second number
            if num1<num2:
                # i add 1 to the ending value, so that the returning dictionary is inclusive of the ending value
                end=num2+1
                #  my i counter, which will be the keys to the nested dictionary questions, starting at 1
                i=1 
                # for every value within this random range
                for var in range(num1,end):
                # return the value in the dictionary at the key given
                    var1=c.get(var)
                    # make a new dictionary with corresponding keys and values
                    ret.update({i:var1})
                    i+=1

            if num2<num1:
                # i add 1 to the ending value, so that the returning dictionary is inclusive of the ending value(in this case its num1)
                end=num1+1
                i=1
                for var in range(num2,end):
                # same logic as the first if statement, except num2 is the staring value in the range this time
                    var1=c.get(var)
                    ret.update({i:var1})
                    i+=1
            return ret
        except:
            return 'Oops a problem has occured'

    def exclude_dictionary_questions(self, line_nums_list):
        '''This method returns the questions, stimuli, and associated answers, 
        in the file in the dictionary format, excluding the question located at the 
        line numbers specified in line_nums_list.'''
        try:
            # getting our nested dictionary again
            c = self.all_dictionary_questions()
            # this will be the dictionary thats returned
            ret = {}
            # getting the amount of lines in the file
            lines=self.line_count()
            # minusing one from lines as we dont count the first line of the file (line 0)
            # as it doesn't have a question
            lines=lines-1
            # my i counter for my first while loop
            i=1
            # my List Of Numbers
            lon=[]
            # my j counter for my second while loop
            j=1
            k=0

            while i<=lines:
                #  i use this while loop to get a list of the numbered lines in the file
                # which in this case is [1,2,3,4,5,6,7]
                lon.append(i)
                i+=1
            
            while j<=lines and j in lon:
                key=lon[k]
                #  while the number j is within line range (not negative) and its in my list of numbers
                if j not in line_nums_list:
                    #  if j is not given as a line to exclude
                    var1 = c.get(j)
                    # get the corresponding values at key j in the nested dictionary
                    ret.update({key:var1})
                    #  update our new dictionary with j as the outer key, with corresponding inner dictionary
                    # this ensures that all lines that haven't been excluded, are added to a new dictionary and returned
                    k+=1
                j+=1
                # incrementing j to check the next line etc..
            return ret
        except:
            return 'Oops a problem has occured'

    def exclude_dictionary_range(self,questions_range:list[int]):
        '''This method returns all of the questions, stimuli and associated 
        answers in the file (in the dictionary format above) excluding the range 
        specified in the list, inclusive of both.'''
        
        try:
            lines=self.line_count()
            # ensuring questions range is a list of integers and that the last value of the range isnt larger than file length
            if all(questions_range)==True and questions_range[1]<lines:
                # my nested dictionary of the file contents
                c = self.all_dictionary_questions()
                # this will be the dictionary thats returned
                exc_ret = {}
                final_ret={}
                i=1
                #  the end will be the second value in the questions_range list + 1 as to include the final line mentioned, in the excluded
                end = questions_range[1]+1
                # for every value in line_nums_list, within range
                for var in range(questions_range[0],end):
                    # return the value in the dictionary at the key/var given
                    var1=c.get(var)
                    # make a new dictionary with range of questions we want to exclude
                    exc_ret.update({var:var1})

                    if var in exc_ret and var in c:
                        #  compare c (origional nested dictionary) and ret (dictionary with range of questions we want excluded)
                        c.pop(var)
                        #  and if a question is in the ret dictionary and must be excluded, we pop/ get rid of it from c

                #  after the first for loop is finished, this one will run, and return c with the keys in consecutive order
                for var in c:
                    var1=c.get(var)
                    final_ret.update({i:var1})
                    i+=1

                #  andwe return the final dictionary with the non excluded questions
                return final_ret

            else:
                return 'Oops an error has occured. Please ensure questions_range is of type list, containing only 2 integers, and that the ending value is not greater than the length of the file'
        except:
            return 'Oops a problem has occured'