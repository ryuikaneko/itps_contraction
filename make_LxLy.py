#!/usr/bin/env python

from __future__ import print_function

import numpy as np
import scipy as scipy
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='make tensors')
    parser.add_argument('-Lx',metavar='Lx',dest='Lx',type=int,default=2,help='set Lx')
    parser.add_argument('-Ly',metavar='Ly',dest='Ly',type=int,default=2,help='set Ly')
    return parser.parse_args()

def make_tensors(Lx,Ly):
    print("# Lx x Ly site contraction (Lx="+str(Lx)+", Ly="+str(Ly)+")")
    print("")

    print("## def Contract_scalar_"+str(Lx)+"x"+str(Ly)+"(\\")
    for y in range(Ly+1,-1,-1):
        print("##     ",end="")
        for x in range(0,Lx+2):
            print("t"+str(x)+"_"+str(y),end="")
            print(",",end="")
        print("\\")
    for y in range(Ly,0,-1):
        print("##     ",end="")
        for x in range(1,Lx+1):
            print("o"+str(x)+"_"+str(y),end="")
            if x!=Lx or y!=1:
                print(",",end="")
        print("\\")
    print("##     ):")

    print("")

## 2
## |
## LB--1
    x = 0
    y = 0
    print("tensor",end=" ")
    print("t"+str(x)+"_"+str(y),end=" ")
    print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
    print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
    print("")

##     1
##     |
## 2--RB
    x = Lx+1
    y = 0
    print("tensor",end=" ")
    print("t"+str(x)+"_"+str(y),end=" ")
    print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
    print("b"+"t"+str(x-1)+"_"+str(y)+"t"+str(x)+"_"+str(y),end=" ")
    print("")

## LT--2
## |
## 1
    x = 0
    y = Ly+1
    print("tensor",end=" ")
    print("t"+str(x)+"_"+str(y),end=" ")
    print("b"+"t"+str(x)+"_"+str(y-1)+"t"+str(x)+"_"+str(y),end=" ")
    print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
    print("")

## 1--RT
##     |
##     2
    x = Lx+1
    y = Ly+1
    print("tensor",end=" ")
    print("t"+str(x)+"_"+str(y),end=" ")
    print("b"+"t"+str(x-1)+"_"+str(y)+"t"+str(x)+"_"+str(y),end=" ")
    print("b"+"t"+str(x)+"_"+str(y-1)+"t"+str(x)+"_"+str(y),end=" ")
    print("")

## 4(c) 3
##   \ /
##    v
## 2--B--1
    y = 0
    for x in range(1,Lx+1):
        print("tensor",end=" ")
        print("t"+str(x)+"_"+str(y),end=" ")
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
        print("b"+"t"+str(x-1)+"_"+str(y)+"t"+str(x)+"_"+str(y),end=" ")
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
        print("bc"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
        print("")

## 2  4(c)
## | /
## L<
## | \
## 1  3
    x = 0
    for y in range(1,Ly+1):
        print("tensor",end=" ")
        print("t"+str(x)+"_"+str(y),end=" ")
        print("b"+"t"+str(x)+"_"+str(y-1)+"t"+str(x)+"_"+str(y),end=" ")
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
        print("bc"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
        print("")

## 1--T--2
##    ^
##   / \
##  3 4(c)
    y = Ly+1
    for x in range(1,Lx+1):
        print("tensor",end=" ")
        print("t"+str(x)+"_"+str(y),end=" ")
        print("b"+"t"+str(x-1)+"_"+str(y)+"t"+str(x)+"_"+str(y),end=" ")
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
        print("b"+"t"+str(x)+"_"+str(y-1)+"t"+str(x)+"_"+str(y),end=" ")
        print("bc"+"t"+str(x)+"_"+str(y-1)+"t"+str(x)+"_"+str(y),end=" ")
        print("")

##   3  1
##    \ |
##     >R
##    / |
## 4(c) 2
    x = Lx+1
    for y in range(1,Ly+1):
        print("tensor",end=" ")
        print("t"+str(x)+"_"+str(y),end=" ")
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
        print("b"+"t"+str(x)+"_"+str(y-1)+"t"+str(x)+"_"+str(y),end=" ")
        print("b"+"t"+str(x-1)+"_"+str(y)+"t"+str(x)+"_"+str(y),end=" ")
        print("bc"+"t"+str(x-1)+"_"+str(y)+"t"+str(x)+"_"+str(y),end=" ")
        print("")

## mid t
##
##    2
##    |
## 1--T--3
##    |\
##    4 5
    for y in range(1,Ly+1):
        for x in range(1,Lx+1):
            print("tensor",end=" ")
            print("t"+str(x)+"_"+str(y),end=" ")
            print("b"+"t"+str(x-1)+"_"+str(y)+"t"+str(x)+"_"+str(y),end=" ")
            print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
            print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
            print("b"+"t"+str(x)+"_"+str(y-1)+"t"+str(x)+"_"+str(y),end=" ")
            print("m"+str(x)+"_"+str(y),end=" ")
            print("")

## mid tc
##
##    2
##    |
## 1--T--3
##    |\
##    4 5
    for y in range(1,Ly+1):
        for x in range(1,Lx+1):
            print("tensor",end=" ")
            print("t"+str(x)+"_"+str(y)+"_conj",end=" ")
            print("bc"+"t"+str(x-1)+"_"+str(y)+"t"+str(x)+"_"+str(y),end=" ")
            print("bc"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
            print("bc"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
            print("bc"+"t"+str(x)+"_"+str(y-1)+"t"+str(x)+"_"+str(y),end=" ")
            print("mc"+str(x)+"_"+str(y),end=" ")
            print("")

## mid o
##
##  1
##  |
##  o
##  |
## 2(c)
    for y in range(1,Ly+1):
        for x in range(1,Lx+1):
            print("tensor",end=" ")
            print("o"+str(x)+"_"+str(y),end=" ")
            print("m"+str(x)+"_"+str(y),end=" ")
            print("mc"+str(x)+"_"+str(y),end=" ")
            print("")

    print("")

## bdim B
    print("bond_dim",end=" ")
    print("100",end=" ")
    y = 0
    for x in range(0,Lx+1):
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
    print("")

## bdim L
    print("bond_dim",end=" ")
    print("100",end=" ")
    x = 0
    for y in range(0,Ly+1):
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
    print("")

## bdim T
    print("bond_dim",end=" ")
    print("100",end=" ")
    y = Ly+1
    for x in range(0,Lx+1):
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
    print("")

## bdim R
    print("bond_dim",end=" ")
    print("100",end=" ")
    x = Lx+1
    for y in range(0,Ly+1):
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
    print("")

## bdim B2
    print("bond_dim",end=" ")
    print("10",end=" ")
    y = 0
    for x in range(1,Lx+1):
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
        print("bc"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
    print("")

## bdim L2
    print("bond_dim",end=" ")
    print("10",end=" ")
    x = 0
    for y in range(1,Ly+1):
        print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
        print("bc"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
    print("")

## bdim mid t
    for y in range(1,Ly+1):
        for x in range(1,Lx+1):
            print("bond_dim",end=" ")
            print("10",end=" ")
            print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
            print("bc"+"t"+str(x)+"_"+str(y)+"t"+str(x+1)+"_"+str(y),end=" ")
            print("b"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
            print("bc"+"t"+str(x)+"_"+str(y)+"t"+str(x)+"_"+str(y+1),end=" ")
            print("")

## bdim mid o
    for y in range(1,Ly+1):
        for x in range(1,Lx+1):
            print("bond_dim",end=" ")
            print("2",end=" ")
            print("m"+str(x)+"_"+str(y),end=" ")
            print("mc"+str(x)+"_"+str(y),end=" ")
            print("")

def main():
    args = parse_args()
    Lx = args.Lx
    Ly = args.Ly
    make_tensors(Lx,Ly)

if __name__ == "__main__":
    main()
