#!/usr/bin/env python
# -*- coding: utf-8 -*-

input()
print(len(set(("".join(sorted(set(x))) for x in input().split()))))
