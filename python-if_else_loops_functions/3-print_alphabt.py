#!/usr/bin/python3

for code in range(97, 123):
    if code == 101 or code == 113:
        continue
    else:
        print("{}".format(chr(code)), end='')
