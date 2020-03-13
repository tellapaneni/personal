# this program replicates the popular program called Hangman
# a random word is collected from the dictionary and the user is given the option to enter the characters
# User inputs characters and if they are present, nothing happens, otherwise the man is hanged

# generate random word
from random_word import RandomWords
import string

def removeDupWithoutOrder(str):
    # set() --> A Set is an unordered collection
    #            data type that is iterable, mutable,
    #            and has no duplicate elements.
    # "".join() --> It joins two adjacent elements in
    #               iterable with any symbol defined in
    #               "" ( double quotes ) and returns a
    #               single string
    return "".join(set(str))
# code to get a random word from dictionary
def get_random():
    global randomWord
    global randomWord1
    r = RandomWords()
    randomWord= r.get_random_word(hasDictionaryDef="true",includePartOfSpeech="noun,verb",
                       minDictionaryCount=1, maxDictionaryCount=10,
                      minLength=4, maxLength=4)
    randomWord = randomWord.lower()
  #  print(randomWord)
    randomWord1 = randomWord
    randomWord = removeDupWithoutOrder(randomWord)

# input one character from user & check for numbers, punctuations
# check if already guessed
alreadyGuessed = ''
correctGuesses =''
def check_input():
    global guessInLower
    global alreadyGuessed
    userInput = input('Enter the Character, The characters correctly guessed so far are '+correctGuesses+ ": ")
    if len(userInput) == 1:
        if userInput in (string.digits or string.punctuation):
            print ('Please enter only letters')
            return False
    else:
        print ('Please enter only one character')
        return False
    guessInLower = userInput.lower()
    if alreadyGuessed.find(guessInLower) != -1:
        print ('This character is already entered, try again')
        return False
    else:
        alreadyGuessed = alreadyGuessed + guessInLower
        return True

# function to define the hangman photo
def hangman_photo(i):
       switcher={
               0:'|',
               1:'| \n|',
               2:'| \n| \n|',
               3:'| \n| \n| \n|',
               4:'| \n| \n| \n| \n|',
               5:'| \n| \n| \n| \n| \n|',
               6:'---\n| \n| \n| \n| \n| \n| ',
               7:'------\n| \n| \n| \n| \n| \n| ',
               8:'---------\n| \n| \n| \n| \n| \n| ',
               9:'---------\n|' + " "*7 + "|"+  '\n| \n| \n| \n| \n| ',
               10:'---------\n|' + " " * 7 + "|" + '\n|'+ " " * 7 + "|" + '\n| \n| \n| \n| ',
               11:'---------\n|' + " " * 7 + "|" + '\n|' + " " * 7 + "|" + '\n|' + " " * 7 + "O" + ' \n| \n| \n| ',
               12:'---------\n|' + " " * 7 + "|" + '\n|' + " " * 7 + "|" + '\n|' + " " * 7 + "O" + ' \n|' + " " * 7 + '/\\' + '  \n| \n| ',
               13:'---------\n|' + " " * 7 + "|" + '\n|' + " " * 7 + "|" + '\n|' + " " * 7 + "O" + ' \n|' + " " * 7 + '/\\' + '  \n|' + " " * 7 + '|' + ' \n| ',
            }
       return switcher.get(i)

#Main Engine of the work
def engine(i):
    global randomWord
    global guessInLower
    global correctGuesses
    while not check_input():
        # nothing to do
        print()
    if randomWord.find(guessInLower) == -1:
        return False
    correctGuesses += guessInLower
    return True

# Main Loop
#global alreadyGuessed
global randomWord
get_random()
tries = 0
while True:
    if tries <=14:
        if not engine(tries):
            tries += 1
            print("this is not in the word")
            print(hangman_photo(tries))
        # check to see if the strings are the same

        if sorted(correctGuesses) == sorted(randomWord):
            print("Congratulations you guessed the word")
            print('correct word was ' + randomWord1)
            break
    else:
        print('sorry you exceeded the limit')
        print('correct word was ' +randomWord1)
        break
