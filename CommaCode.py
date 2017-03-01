#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space,
# with and inserted before the last item.

def printlist(l):
    output = ""
    for i in l[:-1]:
        output += i + ", "
    last = ''.join(l[-1:])
    output += "and " + last
    print(output)

spam = ['apples', 'bananas', 'tofu', 'cats']
printlist(spam)