#!/usr/bin/python3
for alphabet in range(122, 96, -1):
    print(chr(alphabet) if alphabet % 2 == 0 else chr(alphabet - 32), end="")
