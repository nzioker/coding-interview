# Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
# five characters, including the null character.)
# My solution
def reverse_string(input_string):
    return ' '.join([i for i in input_string][::-1])




# Second solution
def reverse_string_two(input_string):
    split_string = [i for i in input_string].reverse()
    return split_string

if __name__ == '__main__':
    print(reverse_string_two("palindrome"))