# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %reset
import sys
import networkx as nx

path = r"/home/ubuntu/Documents/taniyanAgac"
sys.path.append(path)
from modules.Veri import Veri
from modules.BaseStructure import BaseStructure
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import numpy as np

#################### parameters ##################################################

b = BaseStructure("", "wavelet domain")
karsilastirma = False
nr_samples = 10000

# %%
# path = r"C:\Users\sebagis\Documents\test1-master"
# os.chdir(path)
#################### parameters ##################################################


def sample_gen():
    sample = {}
    sample["kare"] = {"p": 0.2, "val": [-1, 1, 1, -1]}
    sample["ucgen"] = {"p": 0.2, "val": [-1, -0.5, 0, 0.5, 1, 0.5, 0, -0.5]}
    sample["kare_dalga"] = {"p": 0.1, "val": [0, 0, -1, -1, 1, 1]}

    a = np.linspace(0, 5, 6)
    sample["cos"] = {"p": 0.05, "val": list(np.cos(2 * np.pi * a / len(a)))}
    a = np.linspace(0, 3, 4)
    sample["sin"] = {"p": 0.15, "val": list(np.sin(2 * np.pi * a / len(a)))}
    sample["null"] = {"p": 0.3, "val": [0]}
    return sample





def gen_signal(samples, sample_count):
    borders = [0]
    for key, value in samples.items():
        # plt.plot(value["val"],"-o")
        # print(len(value["val"]))
        borders.append(borders[0] + value["p"])
        borders[0] = borders[-1]
    # plt.legend(samples)
    # plt.show()
    borders = borders[1:]

    signals = []
    for i in samples.keys():
        signals.append([])

    for temp_rand in np.random.rand(sample_count):  # range(sample_count):
        # print("\t", temp_rand)
        for i, border in enumerate(borders):
            if temp_rand < border:
                # print(i, borders[i],temp_rand)
                signals[i].append(list(samples.values())[i]["val"])
                for j, k in enumerate(samples.keys()):
                    if (j != i):
                        signals[j].append(list(np.zeros(len(list(samples.values())[i]["val"]))))
                break
        # print(i, borders[i],temp_rand)
    for i, k in enumerate(samples.keys()):
        signals[i] = [item for sublist in signals[i] for item in sublist]
    return signals

#################### parameters ##################################################
# %%

samples = sample_gen()
signal = gen_signal(samples, nr_samples)

# print(signal)
'''
plt.rc('figure', figsize=(12, 8))
for sig in signal:
    plt.plot(sig)
plt.legend(samples.keys())
plt.show()
'''

# %%

# sinyali topla

signal_raw = []
for i in range(len(signal[1])):
    signal_raw.append(signal[0][i])
    for j in range(3):
        if signal[j + 1][i] != 0:
            signal_raw[-1] = (signal[j + 1][i])
signal_raw_temp = signal_raw

# gurultu ekle
signal_raw = b.v.addNoise(signal_raw, 0, 0.1)


plt.plot(signal_raw_temp)
plt.plot(signal_raw)
plt.show()
# %%


wav_signal = []

window_size = 4
step = 1
window_count = int((len(signal_raw) - window_size + step) / step)



from matplotlib import pyplot as plt
from celluloid import Camera

if False :
    fig = plt.figure()
    camera = Camera(fig)
    plt.rcParams['figure.figsize'] = [15, 10]

for i in range(window_count):
    #temp = b.v.getWaveletCoefs(signal_raw[i*4:(i+1)*4])
    #for i in range(len(temp)):
    #    temp[i]= round(temp[i],2)
    temp = signal_raw[i:i + window_size]
    #print(temp)
    b.tiktakUpdate(temp,)
    if False and (i % b.update_count_limit == b.update_count_limit-1):

        labels = dict((n, d['value']) for n, d in b.agac.nodes(data=True))

        pos = graphviz_layout(b.agac, prog='dot')
        nx.draw_networkx(b.agac, pos=pos, arrows=True, with_labels=True, labels=labels)
        plt.title(str(i))
        plt.draw()
        #plt.show()
        camera.snap()

        pos = graphviz_layout(b.agac, prog='dot')
        nx.draw_networkx(b.agac, pos=pos, arrows=True, with_labels=True, labels=labels)
        plt.legend(str(i))
        #plt.draw()
        # plt.show()
        camera.snap()

    wav_signal.append(temp)
if False:
    animation = camera.animate()
    animation.save('celluloid_minimal.gif', writer = 'imagemagick')

b.clean_tree()

wav_signal = [item for sublist in wav_signal for item in sublist]

# plt.plot(wav_signal)
# plt.show()
# %%


b.plotGraph(short=False)
#b.agCizdir()
print(len(b.agac.nodes))










































