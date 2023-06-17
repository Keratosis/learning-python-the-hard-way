#this is a script that opens and read files
from sys import argv

script , filename = argv

txt = open(filename )
#opens the filename for example array.py

print(f"Here's your file {filename}")
print(txt.read())
#open the file and  prints out the contents

print("Type the filename again:")
file_again = input(" >")

txt_again = open(file_again)
#input the filename again and prints out its contents

print(txt_again.read())

