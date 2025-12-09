#File Hashing

#projects will require File I/O, imported modules, functions, error detection, and command line arguments.
#Create a command line interface for creating and comparing file hash values.  The script will accept a file path and using the hashlib library, generate a hash value for the file and save it to a hashes file, print it to standard out, or both.  The script will also be able to generate a hash value for a file and compare it to the hash value saved in the hashes file.    Use can use 'hashlib.algorithms_available' to determine the supported hashing algorithms.
import argparse
import hashlib
import sys

from functions1 import hashfile, getfilecontents

parser=argparse.ArgumentParser(description="Getting arguments from user")
parser.add_argument('--file',dest="inputfilepath",required=True)
parser.add_argument('--mode',dest="mode",required=True)
parser.add_argument('--stdout',action="store_true",dest="stdout_bool")
args = parser.parse_args()

try:
    inputhash=hashfile(args.inputfilepath)
except:
    print("ERROR PROCESSING INPUT FILE, FILE IS INVALID")
    sys.exit(1)
if args.mode == 'compare':
    try:
        if inputhash == getfilecontents("hashes.txt"):
            print("HASH MATCHES!")
        else:
            print("HASH DOES NOT MATCH!")
    except:
        print("ERROR PROCESSING hashes.txt, FILE IS INVALID")
        sys.exit(1)
if args.mode == 'save':
    try:
        hashesfile = open('hashes.txt','w')
        hashesfile.write(inputhash)
        hashesfile.close()
    except:
        print("ERROR SAVING HASH TO hashes.txt, FILE IS INVALID")
        sys.exit(1)

if args.stdout_bool == True:
    print(inputhash)




'''
mode 1:
get file path;
hash that file;
print to std out or to hashes file or both;

mode 2:
get file path;
hash that file;
compare that hash to the previous hash stored in the hashes file
seems like we can also keep the printing, just add output to hashes as an option for --mode


'''
