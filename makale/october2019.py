# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%reset
import sys
path = r"/home/ubuntu/Documents/taniyanAgac"
sys.path.append(path)
from modules.Veri import Veri
from modules.BaseStructure import BaseStructure

b= BaseStructure("","wavelet domain")

#%%
#path = r"C:\Users\sebagis\Documents\test1-master"
#os.chdir(path)


import numpy as np
def sample_gen():
    sample={}    
    sample["kare"] = {"p":0.2, "val":[-1,1,1,-1] }
    sample["ucgen"]= {"p":0.2,"val":[-1,-0.5,0,0.5, 1,0.5,0,-0.5]}
    sample["kare_dalga"] = {"p":0.1, "val":[0,0,-1,-1,1,1]}
    
    a= np.linspace(0,5,6)
    sample["cos"] = {"p":0.05,"val":list(np.cos(2*np.pi*a/len(a)))}
    a= np.linspace(0,3,4)
    sample["sin"]={"p":0.15,"val":list(np.sin(2*np.pi*a/len(a)))}
    sample["null"] = {"p":0.3,"val":[0]}
    return sample
    
import matplotlib.pyplot as plt
def gen_signal(samples, sample_count):
    
    borders = [0]
    for key,value in samples.items():
        #plt.plot(value["val"],"-o")
        #print(len(value["val"]))
        borders.append(borders[0]+value["p"])
        borders[0]= borders[-1]
    #plt.legend(samples)
    #plt.show()
    borders = borders[1:]
    
    
    signals = []
    for i in samples.keys():
        signals.append([])
    
    for temp_rand in  np.random.rand(sample_count): #range(sample_count):
        #print("\t", temp_rand)
        for i,border in enumerate(borders):
            if temp_rand < border:
                #print(i, borders[i],temp_rand)
                signals[i].append(list(samples.values())[i]["val"])
                for j,k in enumerate(samples.keys()):
                    if(j!=i):
                        signals[j].append(list(np.zeros(len( list(samples.values())[i]["val"]))))
                break
        #print(i, borders[i],temp_rand)
    for i,k in enumerate(samples.keys()):
        signals[i] = [item for sublist in signals[i] for item in sublist]
    return signals


#%%
nr_samples=30

samples = sample_gen()
signal = gen_signal(samples, nr_samples)

#print(signal)
'''
plt.rc('figure', figsize=(12, 8))
for sig in signal:
    plt.plot(sig)
plt.legend(samples.keys())
plt.show()
'''
    
#%%



signal_raw = []
for i in range(len(signal[1])):
     signal_raw.append( signal[0][i])
     for j in range(3):
         if signal[j+1][i]!=0: 
             signal_raw[-1]= (  signal[j+1][i])
             
signal_raw = b.v.addNoise(signal_raw,0,0.4)

#plt.plot(signal_raw)
#%%


wav_signal=[]

window_size = 4
step = 1
window_count = int ( (len(signal_raw)  -window_size + step) / step)

for i in range(window_count):
    #temp = b.v.getWaveletCoefs(signal_raw[i*4:(i+1)*4])
    #for i in range(len(temp)):
    #    temp[i]= round(temp[i],2)
    temp = signal_raw[i:i + window_size]
    #print(temp)
    b.tiktakUpdate(temp,)
    wav_signal.append(temp)
    
wav_signal = [item for sublist in wav_signal for item in sublist]


#plt.plot(wav_signal)
#plt.show()
#%%



b.plotGraph(short=True)
b.agCizdir()
print(len(b.agac.nodes))










































