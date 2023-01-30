import re,datetime
dateRegex = re.compile(r'(\d{,2})/(\d{,2})/(\d{4})')
text = '''Write a regular expression that can detect dates in the DD/MM/YYYY format.Assume that the days range from 01 to 31, the months range from 01to 12, and the years range from 1000 to 2999. Note that if the day or monthis a single digit, it’ll have a leading zero.The regular expression doesn’t have to detect correct days for eachmonth or for leap years; it will accept nonexistent dates like 31/02/2020 or
31/04/2021. Then store these strings into variables named month, day, andyear, and write additional code that can detect if it is a valid date. April,June, September, and November have 30 days, February has 28 days, andthe rest of the months have 31 days. February has 29 days in leap years.Leap years are every year evenly divisible by 4, except for years evenly divisible
by 100, unless the year is 31/04/2021. Then store these strings into variables named month, day, andyear, and write additional code that can detect if it is a valid date. April,June, September, 22/02/1999 and November have 30 days, February has 28 days, andthe rest of the months 13/04/2021 have 31 days. February has 29 days in 12/12/2050 leap years.also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expressionthat can detect a valid date.'''
date = dateRegex.findall(text)
for match in date:
    day = match[0]
    month = match[1]
    year = match[2]
    new_date = day +'/' + month + '/' + year
    try:
        if datetime.datetime(int(year),int(month),int(day)):
            print(new_date + '--> ' + 'valid date' )
    except:
        print(new_date + '--> ' + 'invalid date')


