The purpose of this program is to detect whether a provided number is a valid credit card number.

credit_card_number = ask user for input of the digits #the digits should be between 13 and 16.
digits = make list of the input 
reverse digits

#step one from assignment
evendigits = make list of every second digit from digits
FOR digit in evendigits:
   number1 = digit times two
   number1 = add the numbers from number1 to get a single-digit number
#step two from assignment
   added_numbers = add every number1 with the previous number1 of the FOR loop
print added_numbers

#step three from assignment
odd_digits = make list of odd numbers in digits
number2 = add all the odd digits
print number2


#step four from assignment
total_numbers = added_numbers+ number2

#step five from assignment
IF the remainder of total_numbers divided by 10 is equal to 0:
   print credit card number is valid
ELSE:
   print credit card number is invalid



  


