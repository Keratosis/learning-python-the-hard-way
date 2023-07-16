arr = [1,2,3,4,5,6]
ar2 = 'whats'
revers= ar2[::-1] # reversing the string 

print(revers)


def print_rangoli(size):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    width = (size * 4) - 3
    lines = []
    
    for i in range(size-1, -size, -1):
        line = '-'.join(alphabet[size-1:abs(i):-1] + alphabet[abs(i):size])
        lines.append(line.center(width, '-'))
    
    rangoli = '\n'.join(lines)
    print(rangoli)
    
size = int(input("Enter the size of the rangoli: "))
print_rangoli(size)