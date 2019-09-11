from modules.spektron import *

def specialTrain():
    # feed system with data
    for i in range(20):
        for data in input_data[:5]:
            #print(data)
            s1.addBranchEntropy(data)
    for data in input_data[5:10]:
            #print(data)
            s1.addBranchEntropy(data)


s1 = BaseStructure("input","wavelet domain")

s2 = BaseStructure("next level","wavelet domain")


print("Time domain symbols")
s1.v.displaySymbols()

print()
#print("Wavelet domain symbols")
for i in range(16):
    print(i, s1.v.getWaveletCoefs(s1.v.symbols[i]))
# change all symbols to wavelet domain

#print("Wavelet domain symbols")
#s.v.symbolsToWavelet()
#s.v.displaySymbols()

print ("generate 500 operations, " )
input_data = s1.v.generateInputData(500)
print ("out of witch "+str(len(input_data)/5) + " are valid (i.e. these many result in the range 0-9)")


#s1.v.decodeTrainOperations(input_data)
#print(s.v.genData(["normal",0,10,16],show=True))


nextLevelInput = []
sizeAllowed = 5
print ("Start learning (i.e. feeding the learning structure)")
for data in input_data:
    nod= s1.addBranchEntropy(data)
    #nextLevelInput.append(nod)
    #if(len(nextLevelInput)>sizeAllowed):
    #    nextLevelInput.pop(0)


print("ploting resulting structure")
# #s.agCizdir()
s1.plotGraph( short=False)
print(s1.agac.nodes())
print('number of edges in the graph:', s1.agac.number_of_edges())
print('edges in the graph:', s1.agac.edges())
print('degree counts per node:', s1.agac.degree())


nei = list(s1.agac.neighbors(0))
count = 0
for n in nei:
    print(count, s1.agac.node[n]['value'], s1.agac.node[n]['occurance_count'])
    count+=1
