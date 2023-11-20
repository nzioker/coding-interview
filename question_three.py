"""Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer. NOTE: One or two additional variables are fine.
An extra copy of the array is not."""

def unique_string(str):
    return "".join(set(str))

if __name__ == '__main__':
    print(unique_string("watersss"))