num = int(input("Enter your number: "))

if (num % 3) == 0 and (num % 5) == 0:
    print("FizzBuzz")
elif(num % 3) == 0:
    print("Fizz")
elif(num % 5) ==0:
    print ("Buzz")
else:
    print("The number is not divisible by 3 or 5")

high_income = False
good_credit = True
if high_income and not good_credit:
    print("eligible for loan")
else:
    print("not at all")
#using comparison to define data#
temperature = 29
if temperature > 30:
    print("its a hot day")
elif temperature != 30:
    print("its a cold day")
else:
    print("its neither hot nor cold")

# exercise #
name= 'pamela'

if len(name)<3:
    print("name must be at least 3 characters")
elif len(name)>50:
    print("name must be a maximum of 50 characters")
else:
    print("name looks good")