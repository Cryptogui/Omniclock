import time
import datetime
from datetime import date
again = "True"


while again == "True":
    print ()
    selection = (input("Select mode (case sensitive!):"))
    
    ## Prints mode list
    if selection == "help":
        print ("Modes:")
        print ("dtb: Days to birthday.")
        print ("cd: Current date.")
        print ("ct: Current time")
        print ("ctd: Current time and date")
        print ("exit: Exits the program.")
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

    ## Shows current time
    elif selection == "ct":
        current = time.localtime()
        current_list = list(current)
        (yr, "year", mn, "month", dy, "day", hr, "hour", mi, "minute", s, "second")
        print (current_list)
        print (time.localtime())
        print (date.today())

    ## Exits program
    elif selection == "exit":
        "Shutting down..."
        break

    ## Quite self-explanatory, eh?
    else:
        print ("Invalid entry. Type 'help' for mode list")

