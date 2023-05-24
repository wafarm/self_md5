#!/usr/bin/python3

import hashlib

def main():
    # Generate stub
    file = open("self_md5", "rb").read()
    data = bytes()
    for i in range(32):
        for j in range(4):
            data += open(f"digits/number{i}/bit{j}_0", "rb").read()
    file = replace(file, data)
    
    # Calculate the hash of stub
    md5 = hashlib.md5()
    md5.update(file)
    digest = md5.hexdigest()

    # Generate the real file
    data = bytes()
    for i in range(32):
        md5_digit = int(digest[i], base=16)
        for j in range(4):
            bit = md5_digit % 2
            md5_digit //= 2
            data += open(f"digits/number{i}/bit{j}_{bit}", "rb").read()
    file = replace(file, data)

    # Write the file
    open("result", "wb").write(file)
    
def replace(array1, array2):
    array1 = list(array1)
    for i in range(len(array2)):
        array1[8256 + i] = array2[i]
    return bytes(array1)

if __name__ == "__main__":
    main()