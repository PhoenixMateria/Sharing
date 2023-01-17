def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s.isalnum():
            if (s[0:2].isalpha()):
                if is_mixed_valid(s[2:len(s)]):
                    return True
                    
   

def is_mixed_valid(s): # TC88  0AAA
    for index in range(len(s)):
        if s[index].isnumeric():
            return is_digit_valid(s[index:len(s)])
    return True


def is_digit_valid(s):
    if s.startswith("0"):
        return False
    for c in s:
        if not c.isnumeric():
            return False
    return True


main()