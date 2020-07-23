# Importing hash algorithms - MD5, SHA1, SHA224, SHA256, SHA384, SHA512
import os
from Crypto.Hash import MD5
from Crypto.Hash import SHA1
from Crypto.Hash import SHA224
from Crypto.Hash import SHA256
from Crypto.Hash import SHA384
from Crypto.Hash import SHA512


def get_file_size(fname):
    return os.path.getsize(fname)


# define a function that reads data from a file and hash it.
def get_file_hash(hash_algorithm):
    filename = input("Enter the filename with extension: ")
    h = hash_algorithm.new()
    chunk_size = get_file_size(filename)  # size of file in bytes.

    # getting file's chunk in bytes. 'rb' indicates binary.
    with open(filename, 'rb') as fh:  # rb means file is read in binary  mode i.e. bytes as input for hashing
        while True:
            chunk = fh.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()


# you can provide any hashing algorithm u want
hash_file = get_file_hash(SHA256)
len_hash = len(hash_file)
print("Hash: " + hash_file + "\nand it's length is: " + str(len_hash))