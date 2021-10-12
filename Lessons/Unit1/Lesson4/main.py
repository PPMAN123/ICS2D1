# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-09-29

#Minds On
underOneLitre = float(input("Enter the number of bottles holding less than one litre: "))
overOneLitre = float(input("Enter the number of bottles holding more than one litre: "))
totalRefund = (underOneLitre*.1)+(overOneLitre*.25)
print("Your refund amount is: $", "%.2f" %totalRefund)
print()