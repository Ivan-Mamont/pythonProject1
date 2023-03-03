def scramble(s1, s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    for i in s1:
        if i in s2:
<<<<<<< HEAD
            s1 = s1.replace(i, '')
            print(s1)
    if len(s1) == 0:
        return True
    else:
        return False





print(scramble ('rkqodlw', 'world'))#, True),
#scramble('cedewaraaossoqqyt', 'codewars')#, True),
#scramble('katas', 'steak')#, False),
#scramble('scriptjava', 'javascript')#, True),
#scramble('scriptingjava', 'javascript')#, True)
=======
            i1 = s1.find(i)
            i2 = s2.find(i)
            s1 = s1[:i1] + s1[i1+1:]
            s2 = s2[:i2] + s2[i2+1:]
            print(s1, s2)
    if len(s1) == 0:
        return print('True')
    else:
        return print('False')


scramble('rkqodlw', 'world')#, True),
scramble('cedewaraaossoqqyt', 'codewars')#, True),
scramble('katas', 'steak')#, False),
scramble('scriptjava', 'javascript')#, True),
scramble('scriptingjava', 'javascript')#, True)
>>>>>>> origin/main
