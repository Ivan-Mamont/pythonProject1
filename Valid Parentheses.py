def valid_parentheses(string):
    '''
    Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
    The function should return true if the string is valid, and false if it's invalid.
    '''
    cost1 = 0
    cost2 = 0
    start = string.count('(')
    stop = string.count(')')

    if start != stop:
        print('False')
        return False
    for i in range(len(string)):
        if string[i] == '(':
            cost1 += 1
        elif string[i] == ')':
            cost2 += 1
            if cost2 > cost1:
                print('False')
                return False

    print('True')
    return True






valid_parentheses(" hi)(")# , False, "should work for '  ('")
valid_parentheses(")test") #, False, "should work for ')test'")
valid_parentheses("") #, True, "should work for ''")
valid_parentheses("hi())(") #, False, "should work for 'hi())('")
valid_parentheses("hi(hi)(") #, False, "should work for 'hi(hi)()'")