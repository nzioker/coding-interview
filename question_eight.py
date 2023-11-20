"""Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”)."""

def isSubstring(s1,s2):
    if len(s1) != len(s2):
        return False
    
    concatenated_string_s1 = s1 + s1
    # check whether string 2 occurs in the concatenated string using count
    if concatenated_string_s1.count(s2) > 0:
        return True
    return False
    

if __name__ == '__main__':
    print(isSubstring("AACD", "ACDA"))