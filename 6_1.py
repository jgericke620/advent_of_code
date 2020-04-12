#!/Users/jacogericke/anaconda3/bin/python3

ORBIT_DICT = {"COM": None}

def get_sub_orbits(key, total):
    if ORBIT_DICT[key] == None:
        return total
    else:
        return get_sub_orbits(ORBIT_DICT[key], total+1)
    
   
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
    print(len(ORBIT_DICT.keys()))


    print(sum([get_sub_orbits(k, 0) for k in ORBIT_DICT.keys()]))





if __name__ == "__main__":
    main()