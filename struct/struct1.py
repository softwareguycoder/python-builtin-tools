#!/usr/bin/python

# NOTE: This script utilizes Python 2.7!

import binascii
import struct


# This method prints a structured data val as hex values
# separated by \x in a string, to the console
def print_structured_data(val):
    hexstring = binascii.hexlify(val)
    sx = r"\x" + r"\x".join(hexstring[n : n+2] for n in range(0, len(hexstring), 2))
    print sx
    pass
    
    
# This method packs a list of integers and then prints out the
# hex values that result after the pack operation    
def main():
    a = [5,34,21,75,20]
    val = struct.pack('5B', *a)s
    print_structured_data(val)
    
    
if __name__=="__main__":
    main()
