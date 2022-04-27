import re

def is_valid_IP(strng):
    massiv = strng.split('.')
    pattern = r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'
    pattern2 = r'[0]\d{2}|[0][0]\d{1}|[.][0]\d{1}|^[0]\d+'
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
is_valid_IP('12.255.56.1') #, True)
is_valid_IP('')#, False)
is_valid_IP('abc.def.ghi.jkl')#, False)
is_valid_IP('12.34.56')#, False)
is_valid_IP('12.34.56 .1')#, False)
is_valid_IP('12.34.56.-1')#, False)
is_valid_IP('123.045.067.089')#, False)
is_valid_IP('127.1.1.0')#, True)
is_valid_IP('0.0.0.0')#, True)
is_valid_IP('0.34.82.53')#, True)
is_valid_IP('192.168.1.300')#, False)