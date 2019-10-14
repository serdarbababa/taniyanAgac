import numpy as np
#from pywt import wavedec
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import  graphviz_layout
import networkx as nx
import pandas as pd
import seaborn as sns

from modules.Components import Abstract, Context1, Context2, Actuator, Spektron
from modules.Veri import Veri
from modules.BaseStructure import BaseStructure
#from modulesEski.Utilities import Utilities
#u = Utilities()
#u.playSound(r'C:\serdar\audio\maybe-next-time.wav')          



v = Veri()

inputs = [[[1, 1, 1, 1], [0, 1, 1, 1]],
 [[0, 0, 1, 1], [1, 0, 1, 1]],
 [[1, 1, 1, 1], [0, 1, 1, 1]],
 [[0, 0, 1, 1], [1, 0, 1, 1]],
 [[1, 0, 0, 0], [1, 0, 0, 1]],
 [[1, 0, 0, 0], [1, 0, 0, 1]],
 [[0, 0, 1, 1], [1, 0, 1, 1]],
 [[0, 0, 1, 1], [1, 0, 1, 1]],
 [[0, 0, 1, 1], [1, 0, 1, 1]],
 [[0, 0, 1, 1], [1, 0, 1, 1]]]

for i in range(10):
    print(i,inputs[i])






import numpy as np
from pywt import wavedec
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import networkx as nx
import pandas as pd
import seaborn as sns
import random

import matplotlib.pyplot as plt
import networkx as nx




def addBranch(agac,input_data, counter):
    print(counter)
    poz = 0
    for j in range(len(input_data)): # for all data
        d = input_data[j]

        nei = list(agac.neighbors(poz)) # get neighbours of node with id poz
        if len(nei) == 0: # if there is no node, directly add node
            agac.add_node(counter, value=d, occurance_count=1, id=-1)
            agac.add_edge(poz, counter)
            poz = counter
            counter += 1
        else:
            k = -1
            for n in nei:
                if (agac.node[n]['value'] == d):
                    k = n
                    break
            if (k >= 0):
                poz = k
                agac.node[k]['occurance_count'] += 1
            else:
                agac.add_node(counter, value=d, occurance_count=1, id=-1)
                agac.add_edge(poz, counter)
                poz = counter
                counter += 1
    return poz

def plotGraph(title = "Tree structure", short=False):
    plt.rcParams['figure.figsize'] = [15, 10]
    #labels = dict((n, round(d['value'], 2)) for n, d in agac.nodes(data=True))
    labels = dict((n, d['value']) for n, d in agac.nodes(data=True))
    # pos=nx.graphviz_layout(GG, prog='dot')
    pos = graphviz_layout(agac, prog='dot')
    # nx.spring_layout(GG)

    plt.title(title +" node values")
    nx.draw_networkx(agac, pos=pos, arrows=True, with_labels=True, labels=labels)
    plt.show()
    if (short):
        return
    plt.title("node ids")
    nx.draw_networkx(agac, pos=pos, arrows=True, with_labels=True)
    plt.show()

    plt.title("node frequency")
    labels = dict((n, d['occurance_count']) for n, d in agac.nodes(data=True))
    nx.draw_networkx(agac, pos=pos, arrows=True, with_labels=True, labels=labels)
    plt.show()

    plt.title("final nodes ids")
    labels = dict((n, d['id']) for n, d in agac.nodes(data=True))
    nx.draw_networkx(agac, pos=pos, arrows=True, with_labels=True, labels=labels)
    plt.show()






#agac = nx.DiGraph()
#counter = 1
#agac.add_node(0, value=999999, occurance_count=1, id=-1)


#addBranch(agac,[1,2,3,4],counter)
#addBranch(agac,[1,2,3,4],counter)
#addBranch(agac,[1,2,4,4],counter)

##plotGraph("aha",False)
#nx.draw(agac, with_labels=True)

#plt.show()



ana = BaseStructure()

ana.addBranchEntropy([0,1,2,3,4])
ana.addBranchEntropy([0,1,2,3,4])
ana.addBranchEntropy([0,1,2,3,4])
ana.addBranchEntropy([0,1,2,3,4])
ana.addBranchEntropy([0,1,2,4,4])

ana.agCizdir()



























#data = v.genData(['normal', 10,3,1024*10])
#plt.plot(data)
#plt.show()


class Yapi():
    def __init__(self):
        
        s1Filt=[[0,0,1,1], [1,1,1,1], [1,0,1,0]]
        s2Filt=[[0,0,1,1], [1,1,1,1], [1,0,1,0]]

        genOutput=0

        STM = []
        MTM = []
        LTM = []

        rules = [] 

        output = []
    
    def feed(self,input):
        s = []
        for i in range(len(s1Filt)):
            s1Filt[i] = 1

    def bitwiseOps(self, operation, c1,c2):
        if(operation =='or'):
            print('Bitwise or:  ', [[k | l for k, l in zip(i, j)] for i, j in zip(c1, c2)])
        elif(operation == 'and'):
            print('Bitwise and: ', [[k & l for k, l in zip(i, j)] for i, j in zip(c1, c2)])
        elif(operation == 'not'):
            print('Bitwise and: ', [[k & l for k, l in zip(i, j)] for i, j in zip(c1, c2)])


#############

print("Program is starting")



#inputLen = 1000;

#sample1 = [[0,0,1,1], [1,1,1,1], [1,0,0,0] ]
#sample2 = [[1,0,1,1], [0,1,1,1], [1,0,0,1] ]

#input1 = v.genData(['normal', 100,30,inputLen])

#print(input1[:10])
#inputs= [ [sample1[int(i)%3], sample2[int(i)%3]]  for i in input1]

#print(inputs[:10])
#plt.plot(inputs[:,1])
#plt.show()




#spek= Spektron()

#for i in range(1000):
#    spek.oneBeat(verbose=False)

#operations= spek.getInstantOperationInput()
#[print(i, operations[i]) for i in range(len(operations))]
##for count, item in enumerate(operations):
##    spek.oneBeat(symbol=item, verbose=True)
#for symbol in operations:
#    spek.oneComplexBeat(symbol)
#for symbol in operations[:-1]:
#    spek.checkOperation(symbol)
    
#for i in range(100):
#    operations= spek.getInstantOperationInput()
#    for symbol in operations:
#        spek.oneComplexBeat(symbol)
    
    
#spek.displaySpektron()
