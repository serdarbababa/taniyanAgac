# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %reset
import sys

path = r"/home/ubuntu/Documents/taniyanAgac"
sys.path.append(path)
from modules.BaseStructure import BaseStructure
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import get_window
from modules.Veri import Veri

#################### parameters ##################################################

karsilastirma = False
window_size = 4
step = 1

sample_count = 5000


#################### generate data ##################################################

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


def gen_signal_complex(samples, sample_count):
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


def signal_gen(samples, sample_count):
    borders = [0]
    for key, value in samples.items():
        borders.append(borders[0] + value["p"])
        borders[0] = borders[-1]
    borders = borders[1:]

    signal = []

    for temp_rand in np.random.rand(sample_count):  # range(sample_count):
        for i, border in enumerate(borders):
            if temp_rand < border:
                signal.append(list(samples.values())[i]["val"])
                break
    signal = Veri().mergeList(signal)
    return signal


#################### main  ##################################################
# %%
def ma(nr_samples):
    b = BaseStructure("", "wavelet domain")
    samples = sample_gen()
    signal = signal_gen(samples, nr_samples)

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

    # karsilastimak icin yazdir
    if karsilastirma:
        plt.plot(signal_raw_temp)
        plt.plot(signal_raw)
        plt.show()

    wav_signal = []

    window_count = int((len(signal_raw) - window_size + step) / step)

    for i in range(window_count):
        temp = signal_raw[i:i + window_size]
        b.tiktakUpdate(temp, )

    b.clean_tree()

    wav_signal = [item for sublist in wav_signal for item in sublist]

    # plt.plot(wav_signal)
    # plt.show()
    # %%

    b.plotGraph(short=False)
    # b.agCizdir()
    print(len(b.agac.nodes))


def test():
    m = 128
    b = BaseStructure("", "wavelet domain")
    t = np.arange(m)
    w = get_window('hamming', m)

    # plt.plot(t, w)
    # plt.xlabel("(time) sample #")
    # plt.ylabel("amplitude")
    # plt.title("hamming window")
    # plt.xlim(0, m-1)
    # plt.ylim(-0.025, 1.025)
    # plt.show()

    a = np.linspace(0, 1, m)
    si = 20 * np.sin(3 * 2 * np.pi * a) + 3 * np.cos(10 * 2 * np.pi * a)
    output = w * si

    plt.plot(si)
    plt.plot(output)
    plt.legend(["sin", "window"])
    plt.show()

    plt.plot(b.v.getWaveletCoefs(si))
    plt.plot(b.v.getWaveletCoefs(output))
    plt.legend(["sin", "window"])
    plt.show()

    plt.plot(b.v.getWaveletCoefs(si[:64]))
    plt.plot(b.v.getWaveletCoefs(output[:64]))
    plt.legend(["sin", "window"])
    plt.show()


def modular_run(nr_samples, spektron_count):
    layer = []
    for i in range(spektron_count):
        layer.append(BaseStructure("", "wavelet domain"))

    samples = sample_gen()
    signal = signal_gen(samples, nr_samples)
    #####################################################3
    signal = layer[0].v.addNoise(signal, 0, 0.1)
    #####################################################3
    window_count = int((len(signal) - window_size + step) / step)
    print("window count = ", window_count)
    for i in range(window_count):
        temp = signal[i:i + window_size]
        output_l0 = layer[0].tiktakUpdate(temp)
    layer[0].clean_tree()
    layer[0].plotGraph(short=False)


def initializeLayer(samples, nr_samples, layer):

    signal = signal_gen(samples, nr_samples)
    #####################################################3
    signal = layer.v.addNoise(signal, 0, 0.1)
    #####################################################3
    window_count = int((len(signal) - window_size + step) / step)
    print("window count = ", window_count)
    for i in range(window_count):
        temp = signal[i:i + window_size]
        output_l0 = layer.tiktakUpdate(temp)
    layer.clean_tree()
    #layer.plotGraph(short=True)

def feed_foreward(samples, nr_samples, layers):

    signal = signal_gen(samples, nr_samples)
    #####################################################3
    signal = layers[0].v.addNoise(signal, 0, 0.1)
    #####################################################3
    window_count = int((len(signal) - window_size + step) / step)
    print("window count = ", window_count)

    buffers = []
    for i in range(len(layers)):
        buffers.append([])
    for i in range(window_count):
        buffers[0] = signal[i:i + window_size]
        output_l0 = layers[0].tiktakUpdate(buffers[0])

        for j in range(1,len(layers)-1):
            if len(buffers[j])>window_size:
                buffers[j]=buffers[j][1:]
            buffers[j].append(output_l0)
            output_l0 = layers[j].tiktakUpdate(buffers[j])


    for layer in layers:
        layer.clean_tree()

def totatly_modular(samples, spektron_config):
    spektron_count=0
    for i in spektron_config:
        spektron_count+=i
    layer = []
    for i in range(spektron_count):
        if i<spektron_config[0]:
            layer.append(BaseStructure("", "wavelet domain"))
        else:
            layer.append(BaseStructure("", "time domain"))
    for i in range(spektron_config[0]):
        initializeLayer(samples, 5000, layer[i] )
    feed_foreward(samples, 10000, layer)
    ##################  ploting structures #######################3
    for i in range(spektron_config[0]):
        layer[i].plotGraph(short=True, title="Input layer")
    for i in range(spektron_config[1]):
        layer[spektron_config[0]+ i].plotGraph(short=True, title="Mid Layer" + str(i))
    for i in range(spektron_config[-1]):
        layer[spektron_config[0] + i].plotGraph(short=True, title="Output Layer" + str(i))

sampl = sample_gen()
#modular_run(sample_count, 1)
totatly_modular(sampl,[1,2,1])