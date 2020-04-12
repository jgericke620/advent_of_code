#!/Users/jacogericke/anaconda3/bin/python3

ORBIT_DICT = {"COM": None}

def get_sub_orbits(key, path_list):
    if ORBIT_DICT[key] == None:
        return path_list
    else:
        new_path_list = get_sub_orbits(ORBIT_DICT[key], path_list)
        new_path_list.append(key)
        return new_path_list
    
   
def next_orbit():
    with open('orbits.txt', 'r') as f:
        for line in f.readlines():
            yield line.strip()

def main():
    count = 0
    for orbit in next_orbit():
        centre, moon = orbit.split(')')

        count += 1
    
        if moon not in ORBIT_DICT.keys():
            ORBIT_DICT[moon] = centre


    print(f"Done {count}")

    path1 = get_sub_orbits(ORBIT_DICT['YOU'], [])
    path2 = get_sub_orbits(ORBIT_DICT['SAN'], [])

    print(len(path1))
    print(len(path2))

    print(path1[:5], path1[-5:])
    print(path2[:5], path2[-5:])


    for i in range(len(path1)):
        if path1[i] != path2[i]:
            x = len(path1) + len(path2) -i -i
            print(len(path1)-i)
            print(len(path2)-i)
            print(x)
            quit()





if __name__ == "__main__":
    main()