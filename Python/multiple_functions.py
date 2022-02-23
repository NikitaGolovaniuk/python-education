# edit the functions prototype and implementation
def foo(a, b, c, *args):
    print(len(args))

def bar(a, b, c, **kwargs):
    return True if kwargs.get("magicnumber") == 7 else False


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")