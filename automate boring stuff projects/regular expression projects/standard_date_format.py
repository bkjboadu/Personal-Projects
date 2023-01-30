import re,pyperclip,sys
dateRegex = re.compile(r'(\d{1,4})(-|/)(\d{1,4})(-|/)(\d{1,4})')
text = pyperclip.paste()
dates = dateRegex.findall(text)
now_date = []
for date in dates:
    current_date = ''.join(date)
    currentRegex = re.compile(current_date)
    check_list = []
    check_same_status = False
    for i in range(len(date)):
        if i % 2 == 1:
            continue
        else:
            check_list.append(date[i])

    for x in range(len(check_list)):
        if check_list[x] == check_list[x-1]:
            day = check_list[x]
            month = check_list[x-1]
            year = check_list[x-2]
            check_same_status = True
            break
        else:
            continue

    if check_same_status:
        pass
    else:
        for i in range(len(date)):
            if i % 2 == 1:
                continue

            if date[i] == date[i-1]:
                day = date[i]
                month = date[i-1]
                year = date[i + 1]
            else:
                if len(date[i]) == 4:
                    year = date[i]
                elif int(date[i]) > 12:
                    day = date[i]
                else:
                    month = date[i]
    new_date = str(day) + '/' + str(month) + '/' + str(year)
    text = currentRegex.sub(new_date,text)
print(text)

