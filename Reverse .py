n = int(input("Enter the number: "))
rev = 0
while(n>0):
    Remainder = n%10
    rev = (rev*10)+Remainder
    n = int(n/10)
print("Reverse of Number is ", rev)
# to fid reverse of A GIVEN NO FIRST FING REMAINDER = NUM%10
# THAN REV = REV*10+Remainder
# THEN NUM = NUM //10