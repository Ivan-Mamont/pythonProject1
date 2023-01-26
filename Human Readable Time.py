def make_readable(seconds):
    """
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
    """
    h = seconds//3600
    m = (seconds - h*3600)//60
    s = seconds - h*3600 - m*60
    print("%02d:%02d:%02d" % (h, m, s))
    return ("%02d:%02d:%02d" % (h, m, s))







make_readable(0)# , "00:00:00")
make_readable(5)# , "00:00:05")
make_readable(60)# , "00:01:00")
make_readable(86399)# , "23:59:59")
make_readable(359999)# , "99:59:59")