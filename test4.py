from datetime import datetime

result = []
with open('diary.txt', 'r') as file:
        i = 0
        for line in file:
            if line !='\n':
                result.append(line)

            i += 1
            # print(datetime.strptime(line.strip(), '%d.%m.%Y; %H:%M'))
            # try:
            #     my_day = datetime.strptime(line.strip(), '%d.%m.%Y; %H:%M')
            #     result.append(my_day)
            #     print(result)
            # except:
            #     result[my_day][line]
            print(result)