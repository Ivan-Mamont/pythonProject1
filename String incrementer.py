def increment_string(strng):
    if strng.isalpha() or strng == '':
        strng += '1'
    else:
        for i in range(len(strng)):
            if strng[i:].isdigit():
                chislo = strng[i:]
                stroka = strng[:i]
                cifra = int(chislo)
                nuli = len(chislo) - len(str(cifra))
                if len(str(cifra)) == len(str(cifra+1)):
                    strng = stroka + '0'*nuli + str(cifra+1)

                else: strng = stroka + '0'*(nuli-1) + str(cifra+1)
                break

    print(strng)
    return strng


#increment_string("foo")#, "foo1")
increment_string("foobar001")#, "foobar002")
#increment_string("foobar1")#, "foobar2")
#increment_string("foobar00")#, "foobar01")
#increment_string("foobar99")#, "foobar100")
#increment_string("foobar099")#, "foobar100")
#increment_string("")#, "1")