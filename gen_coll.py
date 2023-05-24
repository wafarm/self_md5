#!/usr/bin/python3

import os, subprocess
import hashlib
import sys
import shutil

def get_filesize(file: str):
    return os.path.getsize(file)

prefix_size = get_filesize("prefix")
fastcoll_path = "./md5_fastcoll"


def coll(file: str):
    coll1 = file + "_1"
    coll2 = file + "_2"

    # Generate
    subprocess.run([fastcoll_path, "-p", file, "-o", coll1, coll2])

    # Padding
    coll1_size = get_filesize(coll1) - prefix_size
    coll2_size = get_filesize(coll2) - prefix_size

    identical = open(coll1, "rb").read()[-128:]

    print(coll1_size, coll2_size)

    open(coll1, "ab").write(identical)
    open(coll2, "ab").write(identical)

    # Check
    print("Checking files...", end='')

    md5_1 = hashlib.md5()
    md5_1.update(open(coll1, "rb").read())

    md5_2 = hashlib.md5()
    md5_2.update(open(coll2, "rb").read())

    if md5_1.hexdigest() != md5_2.hexdigest():
        print("Error!")
        sys.exit(1)
    else:
        print("Done")
    
    open("bit1", "wb").write(open(coll1, "rb").read()[-256:])
    open("bit0", "wb").write(open(coll2, "rb").read()[-256:])

    os.remove(coll1)
    os.remove(coll2)

def main():
    tmp = "tmp"
    shutil.copyfile("prefix", tmp)
    if not os.path.exists("digits"):
        os.mkdir("digits")
    for i in range(32):
        if not os.path.exists(f"digits/number{i}"):
            os.mkdir(f"digits/number{i}")
        for j in range(4):
            print(f"Generating number {i} bit {j}")
            coll(tmp)
            open(tmp, "ab").write(open("bit0", "rb").read())
            shutil.move("bit1", f"digits/number{i}/bit{j}_1")
            shutil.move("bit0", f"digits/number{i}/bit{j}_0")
            

if __name__ == "__main__":
    main()