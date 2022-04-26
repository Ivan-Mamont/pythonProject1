import re

def is_valid_IP(strng):
    massiv = strng.split('.')
    pattern = r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'
    pattern2 = r'[0]\d{1,2}'
    if re.search(pattern2, strng):
        print('1',False)
        return False
    if re.fullmatch(pattern, strng):
        for i in massiv:
            if int(i) > 255:
                print(False)
                return False
        print(True)
        return True
    print(False)
    return False


is_valid_IP('147.207.139.237')
