def scramble(s1, s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    for i in s1:
        if i in s2:
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