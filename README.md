# Python-Module-Assignment
Hello this is my Python Module Assignment i chose the assignment "File Hashing"

## About
This Python script will take an input file, hash that file then do the following with that hash: store it, print it or compare it to the currently stored hash

main.py usage:
  Flags:
    --file      Input File to be hashed  
    --mode      mode of operation, 'save' or 'compare'. save will save the file to ./hashes.txt in the current working directory,  
                compare will compare the hash of the input file to the hash stored in ./hashes.txt  
    --stdout    print hash/compare status to standard output  



## Reflection:
I found that working with hashlib was a lot more challenging than I thought it would be, mainly because buffering had to be disabled and the file to be hashed had to be opened in binary mode.
It was quite rewarding to overcome that issue. It helped me to do a python project like this as i had to think about the incorporation of multiple features into this one program and how to tackle that in a way that would be sensible for the user, thinking this way made me simplify the flags and make the user experience better for others.
