from modules.spektron import *

def specialTrain():
    # feed system with data
    for i in range(20):
        for data in input_data[:5]:
            #print(data)
            s.addBranchEntropy(data)
    for data in input_data[5:10]:
            #print(data)
            s.addBranchEntropy(data)


s = BaseStructure("wavelet domain")

print("Time domain symbols")
s.v.displaySymbols()

for i in range(16):
    print(i, s.v.getWaveletCoefs(s.v.symbols[i]))
# change all symbols to wavelet domain
#print("Wavelet domain symbols")
#s.v.symbolsToWavelet()
#s.v.displaySymbols()

input_data = s.v.generateInputData(500)

#s.v.decodeTrainOperations(input_data)

#print(s.v.genData(["normal",0,10,16],show=True))

for data in input_data:
    s.addBranchEntropy(data)
# #s.agCizdir()
s.plotGraph( short=True)

# nei = list(s.agac.neighbors(0))
# count = 0
# for n in nei:
#     print(count, s.agac.node[n]['value'],  s.agac.node[n]['occurance_count'] )
#     count+=1
