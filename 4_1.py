#!/Users/jacogericke/anaconda3/bin/python3

# However, they do remember a few key facts about the password:

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).


RANGE = range(193651,649730)
# Two adjacent digits are the same (like 22 in 122345)
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)

passwords = []

for i in RANGE:
    ps = str(i)
    lst = None
    double = False
    smaller = False

    for c in ps:
        if lst != None:
            if c == lst:
                #print(f"DOUBLE {i}      {lst}{c}")
                double = True
            if int(c) < int(lst):
                #print(f"SMALLR {i}      {lst}{c}")
                smaller = True
        lst = c
    if double == True and smaller == False:
        print(i)
        passwords.append(i)


print(len(passwords))
