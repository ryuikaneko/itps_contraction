#!/bin/bash

function make_input
{
  Lx=$1
  Ly=$2
  ./make_LxLy.py -Lx ${Lx} -Ly ${Ly} > input_Lx${Lx}Ly${Ly}.dat
}

make_input 1 1

make_input 1 2
make_input 2 1

make_input 1 3
make_input 2 2
make_input 3 1

#make_input 1 4
#make_input 2 3
#make_input 3 2
#make_input 4 1

#make_input 1 5
#make_input 2 4
#make_input 3 3
#make_input 4 2
#make_input 5 1

#make_input 1 6
#make_input 2 5
#make_input 3 4
#make_input 4 3
#make_input 5 2
#make_input 6 1
