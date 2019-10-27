#!/bin/bash

mkdir -p input
mkdir -p output
mkdir -p output_raw
mkdir -p output_python

./make_input.sh
mv input_Lx*Ly*.dat ./input

for i in \
./input/*.dat
do
  j="${i##*/}"
  k=output_${j%.dat}
  l=output_${j%.dat}.py
  if [ -e ./output/${k} ]; then
    echo "# File ${j} exists. Do nothing."
  else
    ./Tensordot/tdt.py ./input/${j} -o ./output/${k}
    cat ./input/${j} | grep "^## " | sed 's/^## //g' > ./output_raw/${l}
    cat ./output/${k} | sed 's/_conj/\.conj()/g' | sed 's/^np\.tensordot(/return np\.tensordot(/g' | sed 's/^/    /g' >> ./output_raw/${l}
  fi
done

./gather_python.sh
