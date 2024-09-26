import hashlib
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description= 'Password Crackler')
parser.add_argument('passfile', type= str, help= 'Name of file containing data in the format name:hashedpass')
parser.add_argument('wordfile', type= str, help= 'Name of file containing a list of possible passwords') 

parser.add_argument('-v', '--verbose', action= 'store_true', help= 'Provides time took to crack each password and quantity of passwords unable to be cracked') #creating a tag -v or --verbose to use later
parser.add_argument('-a', '--argument', type= str, help= 'Type name of hashing algorithm used to hash original password')

args = parser.parse_args()



hashmethod = 'sha256'
if args.argument:
    hashmethod = args.argument 
passfile = args.passfile
wordfile = args.wordfile    

namelist = []   #List of people's names
passhash = []   #List of their hashed passwords
wordlist = []   #wordlist.txt as a list in jill.py
wordhash = []   #hashed passwords from wordlist
output = ''   


file = open(passfile, 'r')  #open file with lines formatted, name:hashedpassword
for line in file.readlines():   #looks through lines
    namelist.append(line.split(':')[0].strip()) #puts names into namelist
    passhash.append(line.split(':')[1].strip()) #puts hashedpasswords into passhash
file.close()

file = open(wordfile, 'r') #open file
for line in file.readlines():   #look at lines
    sha = hashlib.new(hashmethod)   #determines hashing method
    line = line.strip()         #removes all extra blank spaces
    wordlist.append(line)       #turns wordlist.txt into a list in pill.py
    sha.update(line.encode())   #turn strings into byte strings and hash them
    wordhash.append(sha.hexdigest())    #turn hashes into hexa code and adds them to wordhash list
file.close()


for line1, line2,  in zip(namelist, passhash): 
    
    start_time = datetime.now()     #start time for cracking each password
    timestamp = False
    for line3, line4 in zip(wordlist, wordhash):
        if line4 == line2:
            output += f'{line1}:{line3}'
            timestamp = True
        

    end_time = datetime.now()       #end time for cracking each password
    if args.verbose and timestamp == True:
        if timestamp == True:
            output += f' (Completed in {(end_time.microsecond - start_time.microsecond)} microseconds)'
    output += '\n'
    
    
    
    
print(output[:-1])

