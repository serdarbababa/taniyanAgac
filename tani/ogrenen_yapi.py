from modules.spektron import *

s = BaseStructure()

s.v.displaySymbols()
input_data = s.v.generateInputData(2)

for i in input_data:
    print(i)





# from modules.girdi_al import Girdi
# import matplotlib.pyplot as plt
# g= Girdi("symbols")
# g.sygnal_generate("symbols",["fixed",2])
#
# for i in range(16):
#
#     print(i, g.auxiliaryData[0].symbols[i])
# print()
#
# for i in range(int(len(g.veri)/8)):
#     print(i)
#     for j in range(8):
#         print(g.veri[i*8+j],end=" ")
#
#     print()
# print()
#
#
# plt.plot(g.veri)
# plt.show()
#
# g.onisleme("wavelet", [8])
#
#
# plt.plot(g.onislenmis)
#
# plt.show()
#
# for i in range(int(len(g.onislenmis)/8)):
#     print(i)
#     for j in range(8):
#         print( g.onislenmis[i*8+j],end=" ")
#     print()
#
#





#
#
# g= Girdi("sembol")
#
# g.semboller_olustur()
#
# for i,v in enumerate(g.symbol.symbols):
#     print(i, v)
#
# print("Semboller")
# g.symbol.displaySymbols()
#
# g.sygnal_generate()
# for i in range(len(g.ops)):
#     print(i, g.ops[i])
#
#
# for i in range(len(g.ops_symbols)):
#     print(i, g.ops_symbols[i])
#
# a=g.ops_symbols
# b= g.symbol.mergeList(a)
# for i in range(20):
#     print(b[i])














#Temmuz 2019 Ilerleme Sunumu icin
# TODO 1. input data
# TODO 2. preprocessing
# TODO 3. Model

# import numpy as np
# from pywt import wavedec
# import matplotlib.pyplot as plt
# from networkx.drawing.nx_agraph import  graphviz_layout
# import networkx as nx
# import pandas as pd
# import seaborn as sns
#
# plt.rcParams['figure.figsize'] = [25, 20]
#
#
# def genData(param, show = False):
# 	a=[]
# 	if param[0]=="normal":
# 		mu, sigma, s = param[1],   param[2], param[3]
# 		a= np.random.normal(mu, sigma, size=s)
# 	elif param[0]=='uniform':
# 		mi, ma,s=param[1],   param[2], param[3]
# 		a= np.random.uniform(mi, ma, s)
# 	elif param[0]=="poisson":
# 		rate,s=param[1],   param[2]
# 		a = np.random.poisson(rate, s)
# 	if(show):
# 		count, bins, ignored = plt.hist(s, 14, density=True)
# 	return a
#
# def generateOperations(operations_count, Test=False, verbose=False):
#     energy = 0
#     all = []
#     for i in range(operations_count):
#         if (verbose): print(i, end="\t")
#         a = genData(["uniform", 0, 10, 4])
#         a = [int(x) for x in a]
#         if (True):  # Test):
#             a[3] = 0
#
#         all.append(a)
#         # print(int(a[0]) , int(a[1])%4, int(a[2]) ,int(a[3])%2)
#         if (int(a[1]) % 4 == 0 and int(a[3]) % 2 == 0):
#             if (verbose):
#                 print(int(a[0]), "+", int(a[2]), "=", int(a[0]) + int(a[2]))
#         elif (int(a[1]) % 4 == 0 and int(a[3]) % 2 == 1):
#             if (verbose): print(int(a[0]), "+", int(a[2]), "= ?")
#         elif (int(a[1]) % 4 == 1 and int(a[3]) % 2 == 0):
#             if (int(a[2]) < int(a[0])):
#                 if (verbose): print(int(a[0]), "/", int(a[2]), "=", int(int(a[0]) - int(a[2])))
#             else:
#                 if (verbose): print(int(a[0]), "/", int(a[2]), "=", int(int(a[2]) - int(a[0])))
#         elif (int(a[1]) % 4 == 1 and int(a[3]) % 2 == 1):
#             if (verbose): print(int(a[0]), "-", int(a[2]), "= ?")
#
#         elif (int(a[1]) % 4 == 2 and int(a[3]) % 2 == 0):
#             if (verbose): print(int(a[0]), "*", int(a[2]), "=", int(a[0]) * int(a[2]))
#         elif (int(a[1]) % 4 == 2 and int(a[3]) % 2 == 1):
#             if (verbose): print(int(a[0]), "*", int(a[2]), "= ?")
#
#         elif (int(a[1]) % 4 == 3 and int(a[3]) % 2 == 0):
#             if (int(a[2]) != 0):
#                 if (verbose): print(int(a[0]), "/", int(a[2]), "=", int(int(a[0]) / int(a[2])))
#             elif (int(a[0]) != 0):
#                 if (verbose): print(int(a[0]), "/", int(a[2]), "=", int(int(a[2]) / int(a[0])))
#
#         elif (int(a[1]) % 4 == 3 and int(a[3]) % 2 == 1):
#             if (verbose): print(int(a[0]), "/", int(a[2]), "= ?")
#     return all
#
# def decodeOperations(all):
#     for i in range(1):
#         print(i, end="\t")
#         a = all[i]
#         #print(int(a[0]) , int(a[1])%4, int(a[2]) ,int(a[3])%2)
#         if(int(a[1])%4==0 and int(a[3])%2 == 0  ):
#             print(int(a[0]) , "+", int(a[2]) ,"=", int(a[0])  + int(a[2]))
#         elif(int(a[1])%4==0 and int(a[3])%2 == 1 ):
#             print(int(a[0]) , "+", int(a[2]) ,"= ?")
#         elif(int(a[1])%4==1 and int(a[3])%2 == 0  ):
#             if(int(a[2])<int(a[0])):
#                 print(int(a[0]) , "/", int(a[2]) ,"=", int(int(a[0])  - int(a[2])))
#             else:
#                 print(int(a[0]) , "/", int(a[2]) ,"=", int(int(a[2])  - int(a[0])))
#         elif(int(a[1])%4==1 and int(a[3])%2 == 1  ):
#             print(int(a[0]) , "-", int(a[2]) ,"= ?")
#         elif(int(a[1])%4==2 and int(a[3])%2 == 0  ):
#             print(int(a[0]) , "*", int(a[2]) ,"=", int(a[0])  * int(a[2]))
#         elif(int(a[1])%4==2 and int(a[3])%2 == 1 ):
#             print(int(a[0]) , "*", int(a[2]) ,"= ?")
#         elif(int(a[1])%4==3 and int(a[3])%2 == 0  ):
#             if(int(a[2])>0):
#                 print(int(a[0]) , "/", int(a[2]) ,"=", int(int(a[0])  / int(a[2])))
#             else:
#                 print(int(a[0]) , "/", int(a[2]) ,"=", int(int(a[2])  / int(a[0])))
#         elif(int(a[1])%4==3 and int(a[3])%2 == 1  ):
#             print(int(a[0]) , "/", int(a[2]) ,"= ?")
# ops=generateOperations(10)
#
# for i, op in enumerate(ops):
#     print(i,op)
# print(" ops0 = ", ops[0])
# decodeOperations([ops[0]])
