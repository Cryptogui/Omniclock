import time
import datetime
from datetime import date
again = "True"


while again == "True":
    print ()
    selection = (input("Select mode:")).lower()
    
    ## Prints mode list
    if selection == "help":
        print ("Modes:\n"
               "dtb: Days to birthday.\n"
               "cd: Current date.\n"
               "ct: Current time.\n"
               "cdt: Current date and time.\n"
               "exit: Exits the program.")
        continue
    
    ## Days to Birthday
    elif selection == "dtb":
        input_day = (input("Enter day:"))
        input_month = (input("Enter month:"))

        today = date.today()
        birthday = date(today.year, int(input_month), int(input_day))
        if birthday < today:
            birthday = birthday.replace(year = today.year + 1)
        print ("Date entered:", birthday)
        time_to_birthday = abs(birthday - today)
        days_to_birthday = time_to_birthday.days

        print (str(days_to_birthday) + " days to birthday")

    ## Shows current date
    elif selection == "cd":
        today = date.today()
        print (today)
        
    elif selection == "ct":
        current = time.localtime()
        current_list = list(current)
        current_dt = current_list[3:6]
        print ("Current time is:")
        print (str(current_dt[3]) + ":" + str(current_dt[4]) + ":" + str(current_dt[5]))

    ## Shows current date and time
    elif selection == "cdt":
        current = time.localtime()
        current_list = list(current)
        current_dt = current_list[0:6]
        print ("Current date and time is:")
        print (str(date.today()) + " " + str(current_dt[3]) + ":" + str(current_dt[4]) + ":" + str(current_dt[5]))


    ## Exits program
    elif selection == "exit":
        "Shutting down..."
        break

    ## Quite self-explanatory, eh?
    else:
        print ("Invalid entry. Type 'help' for mode list")

##remember time.localtime()
##time.struct_time(tm_year=2015, tm_mon=12, tm_mday=22,
##tm_hour=23,tm_min=37, tm_sec=45,
##tm_wday=1, tm_yday=356, tm_isdst=0)
