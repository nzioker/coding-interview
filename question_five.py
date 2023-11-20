# Write a method to replace all spaces in a string with ‘%20’.

# My solution

def space_replacer(str):
    return str.replace(" ", "%20")

if __name__ == '__main__':
    print(space_replacer("I am a test sentence."))