"""
This code is written by "dknaix"
dependencies: Crypto,os,MD5
WIll return Hash values for a input file
For querres conatct: dknaix.github@gamil.com
"""


import os
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
        print("\nFile path incorrect....")
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
        print("\nFile path incorrect....")
        print("Exiting....")
        exit()


path=input("Enter path of file to get CHKSUM: ")
md5_ans=file_checksum_md5(path)
sha256_ans=file_checksum_sha256(path)
print("MD5: "+md5_ans)
print("SHA256: "+sha256_ans)
input("Exit??")
