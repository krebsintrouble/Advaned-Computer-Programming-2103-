name= input("Enter the father's name:")
birthplace = input("Enter Birthplace:")
import datetime

birth_month= int(input("Enter birth month(MM):"))
birth_date= int(input("Enter birth date(DD):"))
birth_year= int(input("Enter birth year(YYYY):"))

today = datetime.date.today()
age=today.year-bith_year-((today.month,today.day)<(birth_month,birth_date))

print("He is", age, "years old")
