#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os.path

print "Digite un numero "

try:
    x = int(raw_input())
except ValueError:
    print "Cantidad invalida!"
    exit()

print "Digite el error."

try:
    err = float(raw_input())
except ValueError:
    print "Cantidad invalida!"
    exit()

print numero

"""
numero = int(raw_input())

if numero.isdigit()

print "Digite el error aceptable para aproxiamar la función"

err = float(raw_input())

print numero, err
"""
