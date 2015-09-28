#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by Thiago Vieira

from random import randint

arq = open("input", "r")
filecontent = arq.readlines()
lines = len(filecontent)

randline = randint(0, lines-1)
lineContent = filecontent[randline]
print lineContent
arq.close()

