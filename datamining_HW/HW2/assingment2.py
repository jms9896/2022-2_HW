'''
 2015251165 정민성
 Assignment 2, Clustering by k-Means


 k = 10 k-means

 Use Euclidean distance

 output에는 각 cluster의 유전자 ID가 필요.
 "6: 0 24 56 139 285 471" "{클러스터 사이즈}: {ID1} {ID2} {ID3} {ID4} {ID5} {ID6}"
 where '6' is the cluster size
 and "0 24 56 139 285 471" are the six gene IDs in the cluster

 each row represents each gene
 each column represents the time point
 Use the row number starting from 0 as a gene ID.

 Round the Euclidean distance and the mean points to 3 decimal places.

 cmder 가서
 "
 python ./assingment2.py assignment2_input.txt
 "
 치면 실행됩니다.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import assignment2_funtion
import sys

#모듈화 나중에합시다.

def main(args): # CLI Arguments로 파일 불러오기
    with open(args, 'r', encoding='UTF-8') as file:
        global genes_full
        global genes_slice
        genes_full = file.read().split()
        genes_slice = []
        #len(genes_full) == 6000
        for i in range(len(genes_full) % 12):
            if i//12==0:
                genes_slice.append([])
            genes_slice[i%12].append(genes_full[i])
        print(genes_slice)
if __name__ == '__main__':
   main(sys.argv[1])

# 전체 데이터 들어있는 genes_full
# 12개로 쪼개어져 들어있는 genes_slice






#assignment2_funtion.main(sys.argv[1])

#df = pd.DataFrame(row = ['time_serial'], columns=['time_point'])


# for i in range(len(genes_full) % 12):
#     for j in range(len(genes_full):
#         df.loc[i].append(genes_full[j])