name=input("enter the name of the employee:")
year_of_service=int(input("enter the no.of.year of service:"))
salary=int(input("enter the salary:"))

if year_of_service>10:
     bonus=salary*(10/100)
     print("bonus amount is:",bonus)

elif year_of_service>6:
     bonus=salary*(8/100)
     print("bonus amount is:",bonus)

elif year_of_service<6:
     bonus=salary*(5/100)
     print("bonus amount is:",bonus)

else:
     print("don't have enough years of experience")

    