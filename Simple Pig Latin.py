def pig_it(text):
    '''
    Move the first letter of each word to the end of it,
    then add "ay" to the end of the word. Leave punctuation marks untouched.
    '''
    st = text.split()
    result = []
    for i in st:
        if i.isalpha():
            result.append(i[1:] + i[0] + 'ay' )
        else:
            result.append(i)
    return(' '.join(result))



pig_it('Pig latin is cool') #, 'igPay atinlay siay oolcay')
pig_it('This is my string') #, 'hisTay siay ymay tringsay')