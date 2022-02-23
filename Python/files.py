# play with files
f = open('deleteit.txt', 'w')
data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do " \
       "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim" \
       " ad minim veniam, quis nostrud exercitation ullamco laboris nisi" \
       " ut aliquip ex ea commodo consequat. Duis aute irure dolor in " \
       "reprehenderit in voluptate velit esse cillum dolore eu fugiat " \
       "nulla pariatur. Excepteur sint occaecat cupidatat non proident, " \
       "sunt in culpa qui officia deserunt mollit anim id est laborum."
f.write(data)
f.close()
# read
f = open('deleteit.txt', 'r')
z = open('deleteit.txt', 'r')
#print(f.read())
print(f.readline(11))
print(z.readline(15))
print(f.readline(6))
f.close()
z.close()

#iterating over each line

with open('deleteit.txt', 'r') as reader:
       line = reader.readline(10)
       while line != '':
              #print(line)
              print(line + ' <--what is going on-->\n', end='')
              line = reader.readline(5)