def Check_LeapYear(Year):  
  if((Year % 400 ==0) or (Year % 100 !=0) and (Year % 4 ==0)):   
    print("Given Year {} is a leap Year".format(Year))  
  else:  
    print ("Given Year {} is not a leap Year".format(Year))
  again() 
  
Yr = int(input("Enter Year to check if leap year or not: "))

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        Yr = int(input("Enter Year to check if leap year or not: "))
        Check_LeapYear(Yr)
    elif calc_again.upper() == 'N':
        print()
    else:
        again()

Check_LeapYear(Yr)
