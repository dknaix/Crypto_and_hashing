"""
This code is written by "dknaix"
dependencies: Crypto,os,MD5

This code is command line utility plz run from cmd/terminal only
For querres conatct: dknaix.github@gamil.com
"""

import os
import sys
from Crypto.Hash import MD5,SHA256

def file_checksum_md5(filename):
    h = MD5.new()
    chunk_size = 8192
    try:
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if len(chunk) == 0:
                    break
                h.update(chunk)
        return h.hexdigest()
    except FileNotFoundError:
        print("\nFile path is incorrect!!!")
        print("Exiting....")
        exit()

def file_checksum_sha256(filename):
    h = SHA256.new()
    chunk_size = 8192 
    try:
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if len(chunk) == 0:
                    break
                h.update(chunk)
        return h.hexdigest()
    except FileNotFoundError:
        print("\nFile path is incorrect!!!")
        exit()

try:
    path=sys.argv[1]
except:
    print("\n!!! This is a command line utility run from cmd/terminal !!!")
    print("Exiting....")
    exit()
md5_ans=file_checksum_md5(path)
sha256_ans=file_checksum_sha256(path)
print("\n=====================================")
print("MD5: "+md5_ans)
print("SHA256: "+sha256_ans)

