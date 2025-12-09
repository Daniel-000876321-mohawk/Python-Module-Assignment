import argparse
import hashlib
import sys

def hashfile(filepath):
    #rb to do read and binary mode
    #buffer 0 to stop python from complaining about needing buffering
    fileopen=open(filepath,'rb',buffering=0)
    filecontents=fileopen.read()
    completedhash=hashlib.sha256(filecontents).hexdigest()
    fileopen.close
    return completedhash
def getfilecontents(filepath):
    fileopen=open(filepath,'r')
    filecontents=fileopen.read()
    fileopen.close()
    return filecontents
