#FORMATTING OF  STRING

#the curly braces act as placeholder in the string
formatter =" {} {} {} {}"

# the .format() replaces the placeholder with whatever is passed as an argument
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,True,False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Hell Paradise",
    "is such ",
    "a good anime",
    "i think I'm gonna re-watch it"
))

      