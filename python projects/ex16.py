# close – Closes the file. Like File->Save.. in your editor.
# read – Reads the contents of the file. You can assign the result to a variable.
# readline – Reads just one line of a text file.
# truncate – Empties the file. Watch out if you care about the file.
# write('stuff') – Writes ”stuff” to the file.
# seek(0) – Move the read/write location to the beginning of the file.


from sys import argv

script, filename = argv

print("We're going to erase {filename}.")
print("If you don't want that , hit CTRL-C (^C).")
print("If you do want that ,hit RETURN .")

input('?')

print('opening file ...')
target = open (filename,'w')
# w write
# r read
# a append
    
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going t ask yo for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("And finally, we close it.")
target.close()

