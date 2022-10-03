'''
2015251165 정민성
Assignment 2, Clustering by k-Means


 k = 10 k-means

 Use Euclidean distance

 "6: 0 24 56 139 285 471"
 where '6' is the cluster size
 and "0 24 56 139 285 471" are the six gene IDs in the cluster

 each row represents each gene
 each column represents the time point
 Use the row number starting from 0 as a gene ID.

 Round the Euclidean distance and the mean points to 3 decimal places.

 cmder 가서
 "
 python ./HW2.py assignment2_input.txt
 "
 치면 실행됩니다.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def main(args):
    with open(args, 'r', encoding='UTF-8') as file:
        print(file.read())

if __name__ == '__main__':
    main(sys.argv[1])



df = pd.DataFrame(columns=['x', 'y'])
