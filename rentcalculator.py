#room rent
rent = int(input("Enter the amount of rent="))
#order food for snacks
food = int(input("Enter the amount of snacks ordered="))
#electricity bill
Electricity_spend= int(input("enter the total of electricity spend="))
#charge per unit
charge = int(input("enter the charge per unit="))
total_electricity = Electricity_spend * charge
#total persons
persons = int(input("enter the number of persons living in room="))

output = (rent+food+total_electricity)// persons

print("each person will pay=",output)