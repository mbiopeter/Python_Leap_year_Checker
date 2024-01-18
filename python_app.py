def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year\n")
            else:
                print("Not leap year\n")
        else:
            print("Leap year\n")
    else:
        print("Not leap year\n")
print("PYTHON LEAP YEAR CHECKER" )
print("------------------------")
while True:
    year = int(input("Enter a year: "))
    is_leap_year(year)