#!/usr/bin/python3

import os
import subprocess

def main():
    result = subprocess.run(['strings', '-td', 'self_md5'], stdout=subprocess.PIPE)
    result = result.stdout.decode()
    for line in result.splitlines():
        if "1111111111111111" in line:
            count = int(line.split()[0])
    os.system(f"head -c {count} self_md5 > prefix")


if __name__ == "__main__":
    main()