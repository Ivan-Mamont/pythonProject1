def spin_words(sentence):
    '''Функция, которая принимает строку из одного или нескольких слов
    и возвращает ту же строку, но с перевернутыми всеми словами из пяти или более букв
    '''
    s = sentence.split()
    revers = []
    for i in s:
        if len(i) >= 5:
            revers.append(i[::-1])
        else:
            revers.append(i)
    revers = ' '.join(revers)
    print(revers)
    return revers


spin_words("Welcome") #, "emocleW")
spin_words("to") #, "to")
spin_words("CodeWars") #, "sraWedoC")
spin_words("Hey fellow warriors") #, "Hey wollef sroirraw")
spin_words("This sentence is a sentence") #, "This ecnetnes is a ecnetnes")