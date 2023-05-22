#string and text
 # a variable is  any line of a code where you set a name equal to a value
 
 # assigning  variable to astring or number
types_of_people =10

# using a f-string format to represent a variable  when printing it
x = f"There are {types_of_people} types of people."

binary = 'binary'
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(y)
print(x)

print(f"I said: {x}")
print(f"I also said:'{y}'")

hilarious = False
high =True

#{ } the calibraces act a the placeholder in tyhe string
joke_evaluation ="Isn't that joke so funny?! {}"


# .format() is used to format strings by inserting values into the placeholders within the string
print(joke_evaluation.format(high))

w = "This is the left sode of..."
e = "a string with a right side."

print(w + e)
      
      