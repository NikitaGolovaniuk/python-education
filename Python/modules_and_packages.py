import re

# Your code goes here
find_members = [i for i in dir(re) if "find" in i]
print(sorted(find_members))