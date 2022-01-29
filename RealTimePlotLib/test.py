#!/bin/env python3

import time

def main():
    while True:
        print(time.strftime('%a %H:%M:%S'))
        time.sleep(1)


if __name__ == '__main__':
    main()