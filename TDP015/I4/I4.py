# källor på lista för month_creator http://www.kev.pulo.com.au/pp/TUTORIALS/1b/examples.html
def check_seven(number):
    if number > 7:
        return number%7
    else:
        return number

def month_creator(month):
    if month == 1:
        return 0
    if month == 2:
        return 3
    if month == 3:
        return 3
    if month == 4:
        return 6
    if month == 5:
        return 1
    if month == 6:  
        return 4
    if month == 7:
        return 6
    if month == 8:
        return 2
    if month == 9:
        return 5
    if month == 10:
        return 0
    if month == 11:
        return 3
    if month == 12:
        return 5


def return_list(number):
    if number == 0:
        return ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    if number == 1:
        return [ 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    if number == 2:
        return ['Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon']

    if number == 3:
        return ['Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue']

    if number == 4:
        return ['Thu', 'Fri', 'Sat','Sun', 'Mon', 'Tue', 'Wed' ]

    if number == 5:
        return ['Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu']

    if number == 6:
        return ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']


def day_of_the_week(y,m,d):
    value_sum = check_seven((3-int(str(y)[:2])%4)*2)
    chomp_year_item =  int(str(y)[2:])
    number_of_dozens = chomp_year_item//12
    overplus = chomp_year_item%12
    amount_fours_overplus = overplus//4
    value_sum = overplus+amount_fours_overplus+number_of_dozens+ value_sum
    value_sum = check_seven(value_sum)
    value_sum = (month_creator(m)+value_sum)
    value_sum = check_seven(value_sum)
   
    day = d
    if (y % 4 == 0 and (y %100 != 0 or y % 400 == 0)):
        if(m == 0 or m == 1):
            day = day-1
    value_sum = check_seven(value_sum + day)
   
    print(return_list(value_sum))



day_of_the_week(2016,1,26)


#18/4 = 4hela 2rest (3 -rest)*2
#19/4 = 4hela 3rest (3-rest)*2 = 0
#20/4 = 5hela 0rest (3-rest)*2 = 6
#21/4 = 5hela 1rest (3-rest)*2 = 4
