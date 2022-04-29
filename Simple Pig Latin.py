def pig_it(text):
    st = text.split()
    result = []
    for i in st:
        for b in range(len(i)):


        result.append(i[::-1] + 'ay')
    у = ' '.join(result)
    print(у)






pig_it('Pig latin is cool') #, 'igPay atinlay siay oolcay')
pig_it('This is my string ?') #, 'hisTay siay ymay tringsay')