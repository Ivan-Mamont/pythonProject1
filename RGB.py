def rgb(r, g, b):
    if r < 0: r = 0
    if r > 255: r = 255
    if g < 0: g = 0
    if g > 255: g = 255
    if b < 0: b = 0
    if b > 255: b = 255
    return format(r, '02X')+format(g, '02X')+format(b, '02X')



# rgb(0, 0, 0)#, "000000", "testing zero values")
# rgb(1, 2, 3)#, "010203", "testing near zero values")
# rgb(255, 255, 255)#, "FFFFFF", "testing max values")
# rgb(254, 253, 252)#, "FEFDFC", "testing near max values")
# rgb(-20, 275, 125)#, "00FF7D", "testing out of range values")
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
