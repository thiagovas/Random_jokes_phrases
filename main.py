#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by Thiago Vieira

from random import randint

arq = open("input")
lines = int(arq.readline())

randline = randint(1, lines)
lineContent = ""
for i in range(0, randline):
	lineContent = arq.readline()
print lineContent
arq.close()

