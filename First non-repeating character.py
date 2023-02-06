def first_non_repeating_letter(string):
    new = string.lower()
    for i in range(len(string)):
        if new.count(new[i]) == 1:
            print(string[i])
            return string[i]
    new = ''
    print(new)
    return new

first_non_repeating_letter('a')#, 'a')
first_non_repeating_letter('STress')# 't')
first_non_repeating_letter('moonmen')#, 'e')
first_non_repeating_letter('')#, '')
first_non_repeating_letter('aa')#, '')
