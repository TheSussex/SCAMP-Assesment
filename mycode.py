# This program gives a fibonacci sequence based on the input of the user
# Author- Success Ologunsua

given_num = int(input("How many terms? "))      # accepting input from the user into the (given_num) variable

n1, n2 = 0, 1  # first two terms
count = 0
if given_num <= 0:                              # check if the number of terms is valid
   print("Please enter a valid term")
elif given_num == 1:
   print("Fibonacci sequence up to",given_num,":")
   print(n1)
else:
   print("For a sequence of" + "given_num" + "," + " you have:")
   while count < given_num:
       print(n1)
       nth = n1 + n2
       # interchanging the variable
       n1 = n2
       n2 = nth
       count += 1
