"""
Convert letters to ASCI chars
"""

import sys

polish_letters="ąćęłŁńŃóśŚżŻźŹ"
asci_letters = "acelLnNosSzZzZ"

def main():
    if len(sys.argv) != 2:
        print("Give the full path to file..")
        sys.exit(1)
    return sys.argv[1]

def replaceLetters(line):
    for pl, al in zip(polish_letters, asci_letters):
        line = line.replace(pl, al)
    return line

def readFile(file_name):
    # open and add in memory
    with open(f"{file_name}", "rt") as fin:
        inmemory_file = fin.read()
    return inmemory_file

def execute(file_name, inmemory_file):
    # read from memory and change
    with open(f"{file_name}", "wt") as fout:
        for line in inmemory_file:
            fout.write(replaceLetters(line))
    return "Letters converted.."

# [optional]
# dynamic changes (requires two files)
# not possible to read and write changes in one file on the fly

# fin = open("/tmp/dupa/data.txt", "rt")
# fout = open("/tmp/dupa/out.txt", "wt")

# for line in fin:
# 	fout.write(replace_letters(line))

# fin.close()
# fout.close()

if __name__ == '__main__':
    file_name = main()
    inmemory_file = readFile(file_name)
    print(execute(file_name, inmemory_file))
