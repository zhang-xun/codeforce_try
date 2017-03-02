#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    numbers = input().split("+")
    s = "+".join(sorted(numbers))
    print(s)


if __name__ == "__main__":
    main()
