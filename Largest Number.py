X = int(input("Enter First number "))
Y = int(input("Enter Second number "))
Z = int(input("Enter Third number "))
if (X>Y) & (X>Z):
   l = X
  
elif (Y>X) & (Y>Z):
   l = Y
else:
   l = Z
print("The largest number is : ",l)
