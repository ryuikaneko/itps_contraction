#!/bin/bash

mkdir -p output_python

output=./output_python/PEPS_Basics_Added.py

echo -ne "" > ${output}

echo "# coding:utf-8" >> ${output}
echo "import numpy as np" >> ${output}
echo "import scipy as scipy" >> ${output}
echo "import scipy.linalg as linalg" >> ${output}
echo "import scipy.sparse.linalg as spr_linalg" >> ${output}
echo "import scipy.linalg.interpolative" >> ${output}
echo "from PEPS_Parameters import *" >> ${output}
echo "" >> ${output}

for i in \
./output_raw/output_input_*.py
do
  cat ${i} >> ${output}
  echo "" >> ${output}
done
