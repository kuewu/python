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

    #exercise 2#
weight = int(input("weight: "))
print(weight)
unit = (input("(L)bs or (k)g: "))

if unit.upper=="l":
  converted = weight*0.45
  print(f"you are {converted} kg")

else:
    converted = weight/0.45
    print(f"ypu are {converted} pounds")

#using the while loop#
Guess_count = 1
while Guess_count<= 5:
    print( '*' * Guess_count)
    Guess_count = Guess_count + 1
print("Done")

# lets create a quess game#
secret_number = 9
Guess_count = 0
Guess_limit = 3
while Guess_count< Guess_limit:
  Guess = int (input("Guess: "))
  Guess_count +=1
  if Guess == secret_number:
      print("you won !!!!! HURRAYYYY")
      break
else:
    print("you failed")