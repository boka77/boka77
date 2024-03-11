# Calculate the value of Pi using the Leibniz formula: 
# Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...etc
Pi = 1
i = 0 
n =  int(input("Please Enter the number of terms : "))
while i < n:
    den = i*2 + 3 
# Alternately subtract and add terms based on the index being even or odd 
    if i %  2 == 0:
        Pi -= 1/den
        i += 1 
    else:
        Pi += 1/den
        i += 1
# Multiply by 4 to get the approximate value of Pi and print the result              
Pi *= 4
print("Value of Pi is ",Pi)


