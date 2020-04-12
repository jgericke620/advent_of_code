#!/Users/jacogericke/anaconda3/bin/python3

RANGE = range(193651,649730)

passwords = []

for i in RANGE:
    ps = str(i)
    lst = None
    
    multi_groups = [[], [], [], [], [], []]
    multi_index = 0
    smaller = False


    for c in ps:
        if lst != None:
            if c != lst:
                multi_index += 1

            if int(c) < int(lst):
                smaller = True

        multi_groups[multi_index].append(c)

        lst = c

    if any([len(x)==2 for x in multi_groups]) and smaller == False:
        passwords.append(i)


print(len(passwords))
