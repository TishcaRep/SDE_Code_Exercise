import sys
import json
import os.path

# Author: Julio Romo Tishca
## Github: github.com/TishcaRep
# Twitter: @Tishca_tpx

# Detect if the files exist in the path
# @path_file had the dynamic value of sys.argv[x]


def File_empty(path_file):
    if (os.path.isfile(path_file)):  # Detect Path exists
        if not (Num_Lines(path_file) > 0):  # File is empty ? to didn spent time
            print("The file ", path_file, " is empty")
            sys.exit()
    else:
        print("The file ", path_file, " didn't exist")
        sys.exit()


#Fun to chech file lenght
def Num_Lines(path_file): 
    with open(path_file, 'r') as fp:
        num_lines = sum(1 for line in fp)
        return num_lines

#Fun Save data from files  and return list (This could be used later)
def Storage_Streets(_file):
    lines = []
    with open(_file) as file:
        [lines.append(line.rstrip().upper()) for line in file]
    return lines

#Fun Save data from files  and return array list (Only for drivers)
def Storage_Drivers(_file):
    lines = []
    with open(_file) as file:
        [lines.append({"Driver": line.rstrip().upper(), "Street": "","SS":""})
         for line in file]
    return lines

# Secret algoritm based in the  test
def Secret_Algoritm(streets, drivers):
    vowels = "AEIOU" #Set the Vowels
    if len(streets) == len(drivers): # Detect if drivers and streets are the same case
        print("All ok, Let's go.")
    else:
        if len(drivers) > len(streets): # if  are more drivers than  streets cas
            print("Some drivers could go to home early.")
        else:
            print("Maybe will be need make some deliveries tomorrow.") # More  Streets  than drivers case
    for sid in range((( len(streets), len(drivers) )[len(streets) > len(drivers)], len(streets))[len(streets) == len(drivers)]): #The same if before but using like ternary operators to make less code
        num_vowels = 0 #Set  default vowels value and reset every looṕ
        for _char in drivers[sid]["Driver"]:# Get each char in drivers name
            if _char in vowels: #find the char in vowels array
                num_vowels = num_vowels +1 #add 1 to num_vowels
        num_vowels = num_vowels * (1,1.5)[len(streets[sid])%2 == 0] #Here some calcs magic from the test  using ternary if street name is even (num_vowels *  1.5) else  (num_vowels *  1) || num_vowels 
        drivers[sid]["Street"] = streets[sid] #Just set the destination street
        drivers[sid]["SS"] = (num_vowels,num_vowels*1.5)[len(streets[sid]) ==len(drivers[sid]["Driver"])] # If driver name had the same length of street name multiply 
    return drivers    
    


def main():
    if __name__ == "__main__":
        if (len(sys.argv) != 3):  # Only can get 3  arguments "python" file1 file2
            print("Syntax : python script.py streets.txt drivers.txt")
            sys.exit()
        for inc in range(1, 2): # use for with range for scalability
            File_empty(sys.argv[inc]) # Check if files exist
        streets = Storage_Streets(sys.argv[1]) # Save data in list 
        drivers = Storage_Drivers(sys.argv[2]) # Save data in array list
        drivers_asigned = Secret_Algoritm(streets, drivers) # Run the secret Algoritm 
        print(json.dumps(drivers_asigned, indent=4, sort_keys=True)) # this only to print pretty

main() # Start
