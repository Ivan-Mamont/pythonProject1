
def duplicate_count(text):
    '''
    Write a function that will return the count of distinct case-insensitive alphabetic
    characters and numeric digits that occur more than once in the input string.
    The input string can be assumed to contain only alphabets (both uppercase and lowercase)
    and numeric digits.
    '''
    new_text = text.lower()
    kol = 0
    print(new_text)
    for i in new_text:
        rez = new_text.count(i)
        if rez > 1:
            kol += 1
    itog = kol - (len(new_text) - len(set(new_text)))
    print(itog)




# Your code goes here


duplicate_count("") #, 0)
duplicate_count("abcde") #, 0)
duplicate_count("abcdeaa") #, 1)
duplicate_count("abcdeaB") #, 2)
duplicate_count("Indivisibilities") #, 2)