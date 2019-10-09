import numpy as np
from pywt import wavedec
import matplotlib.pyplot as plt
import pandas as pd
import random



class Veri():
######### generate symbols #######################################
    def genData(self, param, show=False):
        a = []
        if param[0] == "normal":
            mu, sigma, s = param[1], param[2], param[3]
            a = np.random.normal(mu, sigma, size=s)
        elif param[0] == 'uniform':
            mi, ma, s = param[1], param[2], param[3]
            a = np.random.uniform(mi, ma, s)
        elif param[0] == "poisson":
            rate, s = param[1], param[2]
            a = np.random.poisson(rate, s)
        if (show):
            count, bins, ignored = plt.hist(s, 14, density=True)
            plt.show()
        return a

    def genInstantSymbol(self, verbose =False):
        x = self.symbols[ random.randint(0, 15)]
        if verbose: print(x)
        return x
    ########## generate alphabet  ######################################
    def genSample(self, signalCount, verbose=False):
        if verbose: print("generate sample data")
        signals = []
        for i in range(signalCount):
            a = self.genData(["normal", 100, 100, 8])
            # print(a)
            sig = []
            for j in range(8):
                sig.append(int(a[j]))
            signals.append(sig)
        for i in range(signalCount):
            if verbose: print(signals[i])
        return signals

    def getSamplePredef(self):
        #print("return sample data")
        signals = [[105, 220, 23, 99, 266, 190, 37, 5],
                   [334, 174, 134, -7, 19, 155, 93, 89],
                   [72, 96, 102, 151, -14, 171, 127, 127],
                   [15, 38, 283, 204, 232, 141, 121, 47],
                   [157, -60, 54, 54, 69, -27, -14, 101],
                   [0, 113, 74, 176, 68, 322, 135, 367],
                   [56, 114, 126, 181, 93, 41, 118, 76],
                   [164, 200, 351, 51, 36, 163, 298, -5],
                   [140, 124, 99, 34, -46, -5, 240, 136],
                   [113, 58, 130, 123, 171, 143, 109, 17],
                   [-8, 299, 65, 62, 130, 146, -43, 23],
                   [-96, 212, 56, 150, -55, 150, 151, 70],
                   [-22, 148, 219, 62, 108, 136, 198, 126],
                   [220, 84, 165, 167, 1, 227, 15, 144],
                   [200, 135, 165, 64, 100, 224, 244, 140],
                   [21, 183, -161, 65, 33, 257, -16, 112]]
        return signals

############## utilities ##################################
    def mergeList(self, input_data, verbose=False):
        if verbose:
            print("merge data")
        merged_list = []
        for l in input_data:
            merged_list += list(l)
        return merged_list

    ################################################
    def listToPandasDF(self, input_data):
        df = pd.DataFrame(input_data)
        return df

    ################################################
    def getWaveletCoefs(self, input_data):
        coefs = []

        girdi = np.array(input_data)  # np.array([1,2,3,4,5,6,7,8])*1
        coeff = wavedec(girdi, 'haar', level=int(np.log2(len(girdi))))
        coefs = (self.mergeList(coeff))

        for i in range(len(coefs)):
            coefs[i]=round(coefs[i],2)

        return coefs

    ################################################
    def rmse(self, predictions, targets):
        return np.sqrt(((predictions - targets) ** 2).mean())
    ################################################
    def quantize(self, input_data, verbose=False):
        borders = [-200, -100, -50, 0, 50, 100, 200]
        borders = [-6000, -4000, -2000, -1000, -500, -100, -50, 0, 50, 100, 500, 1000, 2000, 4000, 6000]
        #borders = [-100, -50, -30, -20, -10, -5, -3, 0, 3, 5, 10, 20, 30, 50, 100]
        sig = []
        if (verbose):
            print(input_data)
        for j in range(int(len(input_data))):
            output = len(borders)
            for k in range(len(borders)):
                if (input_data[j] < borders[k]):
                    output = k
                    break
            if verbose:
                print(output, " ",)
            sig.append(output)
        if verbose:
            print()
        return sig
    ################################################
    def quantize(self, input_data, borders, verbose=False):
        sig = []
        if (verbose):
            print(input_data)
        for j in range(int(len(input_data))):
            output = len(borders)
            for k in range(len(borders)):
                if (input_data[j] < borders[k]):
                    output = k
                    break
            if verbose:
                print(output, " ",)
            sig.append(output)
        if verbose:
            print()
        return sig


############# generate signal ###################################
    def generateOperationsSymbols(self, operations_count, Test=False, verbose=False):
        ops_ids = []
        symbolSet = []

        for i in range(operations_count):
            if (verbose): print(i, "\t",)
            a = self.genData(["uniform", 0, 10, 4])
            a = [int(x) for x in a]
            if (Test):
                a[3] = 0
            go = True
            # a=[4, 5, 9, -5]

            rez = 0
            if (int(a[1]) % 4 == 0):  # operation is +
                if (a[0] + a[2] > 9):
                    go = False
                else:
                    rez = a[0] + a[2]
            elif (int(a[1]) % 4 == 1):  # operation is -
                if a[0] < a[2]:
                    go = False
                else:
                    # print("here", a[0] - a[2] , a[0] > a[2])
                    rez = a[0] - a[2]
            elif (int(a[1]) % 4 == 2):  # operation is *
                if (a[0] * a[2] > 9):
                    go = False
                else:
                    rez = a[0] * a[2]
            elif (int(a[1]) % 4 == 3):  # operation is -
                if (a[2] == 0):
                    go = False
                else:
                    rez = int(a[0] / a[2])
            # rint(go)
            if go:
                if verbose: print(go, rez)
                a[3] = rez
                ops_ids.append(a)
                symbolSet.append(self.symbols[a[0]])
                symbolSet.append(self.symbols[a[1] % 4 + 10])
                symbolSet.append(self.symbols[a[2]])
                symbolSet.append(self.symbols[14])
                if (not Test):
                    symbolSet.append(self.symbols[a[3]])
                else:
                    symbolSet.append(self.symbols[15])
        return ops_ids, symbolSet


    ################################################
    def generateInputData(self, op_count, verbose=False):
        for i in range(10):
            encoded, symbol_based = self.generateOperationsSymbols(op_count, False, verbose)
            if len(symbol_based)>0:
                break
        if (verbose):
            print("operation symbols")
            for i in range(len(symbol_based)):
                print(i, symbol_based[i])
            print()
        return symbol_based

    ################################################
    def addNoise(self, data, noise_mean, noise_std):
        return data

    def symbolsToWavelet(self):
        v = []
        for i in range(len(self.symbols)):
            v.append(self.getWaveletCoefs(self.symbols[i]))
        self.symbols = v


########## display ######################################
    def displaySymbols(self):
        symbols_correspondence = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "=", "?"]
        print("indice", "symbol", "pattern")
        for i in range(len(self.symbols)):
            print(i,  symbols_correspondence[i],    self.symbols[i])


    def decodeTrainOperations(self,all):
        symbols_correspondence = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "=", "?"]
        for i in range( int(len(all)/5)):
            for j in range(5):
                print(symbols_correspondence[ self.symbols.index(all[i*5+j]) ] ,end=" ")
            print()

############ constructor ####################################
    def __init__(self,tip="input"):
        #self.symbols = self.genSample(16)
        if(tip=="input"):
            self.symbols = self.getSamplePredef()
