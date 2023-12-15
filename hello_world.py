from datetime import datetime
name = input("Enter Your Name: ")
age = input("Enter yob: ")
prof = input ("Enter your profession: ")
conv = int(age)
current_year= datetime.today().year
print('\n')
present_age = current_year-conv
def personal_info():
	print("This is my Introduction,")
	print("I'm "+name+" \nI'm "+ str(present_age)+" year old"+"\nAnd i do is "+prof)

personal_info()


