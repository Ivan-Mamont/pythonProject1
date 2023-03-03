def format_duration(seconds):
    year = seconds // 31536000
    day = (seconds - year*31536000) // 86400
    hour = (seconds - year*31536000 - day*86400) // 3600
    minute =  (seconds - year*31536000 - day*86400 - hour*3600) // 60
    seconds = seconds - year*31536000 - day*86400 - hour*3600 - minute*60
    #print(seconds)
    rezult = ''
    rez = []
    if year != 0:
        if year != 1:
            rez.append([year, 'years'])
        else:
            rez.append([year, 'year'])


    if day != 0:
        if day != 1:
            rez.append([day, 'days'])
        else:
            rez.append([day, 'day'])

    if hour != 0:
        if hour != 1:
            rez.append([hour, 'hours'])
        else:
            rez.append([hour, 'hour'])

    if minute != 0:
        if minute != 1:
            rez.append([minute, 'minutes'])
        else:
            rez.append([minute, 'minute'])

    if seconds != 0:
        if seconds != 1:
            rez.append([seconds, 'seconds'])
        else:
            rez.append([seconds, 'second'])

    z = len(rez)
    for i in range(z):
        if z > 2:
            rezult += str(rez[i][0]) + ' ' + rez[i][1] + ', '
            z -= 1
        elif z == 2:
            rezult += str(rez[-2][0]) + ' ' + rez[-2][1] + ' and ' + str(rez[-1][0]) + ' ' + rez[-1][1]
            z = 0
        elif z == 1:
            rezult += str(rez[-1][0]) + " " + rez[-1][1]
            z = 0
    return rezult







#
format_duration(1)#, "1 second")
format_duration(62)#, "1 minute and 2 seconds")
# format_duration(120)#, "2 minutes")
# format_duration(3600)#, "1 hour")
format_duration(3153504000)#, "1 hour, 1 minute and 2 seconds")