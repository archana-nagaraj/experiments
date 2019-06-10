# control flow : Conditional Statements

# if statement

if True:
    print("hello python")

if 2 > 1:
    print("2 is greater than 1")

#example
a = 33
b = 200
if b > a:
  print("b is greater than a")

###############################################
#  Else statement

if 1 > 2:
    print ("1 is greater than 2")
else:
    print ("1 is not greater than 2")



# elif statement (else if statement)

if 1 > 2:
    print ("1 is greater than 2")
elif 2 > 1:
    print ("2 is greater tha 1")
else:
    print ("1 is equal to 2")


#example 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# example shorthand 
if a > b: print("a is greater than b")
print("A") if a > b else print("B")
if a > b and c > a:
  print("Both conditions are True")

#One line if else statement, with 3 conditions:
print ("this") if a > b else print ("these") if c > a else print "only"

# with or operator
if a > b or a > c:
  print("At least one of the conditions is True")
#############################################

