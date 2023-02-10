#If Statements (LOOPS)
temperature = 9

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:   # (20, 30] i.e temperature is greater than 20 and less than 30
    print("It's a nice day")
elif temperature > 10:  #(10, 20] i.e temperature is greater than 10 and less than 20
    print("It's a bit cold")
else:
    print("It's cold")
#press shift + tab to end the if loop
print("Done")

#Exercise
#Weight: 170
#(K)g or (L)bs: l
#Weight in Kg: 76.5

weight = input("Weight: ")
b = input("(K)g or (L)bs: ")
if b.upper() == "L":
    x = float(weight) * 0.45
    print("Weight in Kg: " + str(x))
elif b.upper() == "K":
    y = float(weight) * 2.2 #float(weight)/0.45
    print("Weight in lbs: " + str(y))
else:
    print("Done")


