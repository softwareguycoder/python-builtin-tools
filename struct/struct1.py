#!/usr/bin/python

# NOTE: This script utilizes Python 2.7!

import binascii
import re
import struct

replchars = re.compile(r'[\n\r]')


def replchars_to_hex(match):
    return r'\x{0:02x}'.format(ord(match.group()))
    

# This method packs a list of integers and then prints out the
# hex values that result after the pack operation    
def main():
    a = [5,34,21,75,20]
    val = struct.pack('5B', *a)
    hexstring = binascii.hexlify(val)
    sx = r"\x" + r"\x".join(hexstring[n : n+2] for n in range(0, len(hexstring), 2))
    print sx
    
    
if __name__=="__main__":
    main()
