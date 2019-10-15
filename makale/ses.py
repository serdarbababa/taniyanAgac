import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)



# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
import re

import matplotlib.pyplot as plt

import IPython.display as ipd  # To play sound in the notebook
import scipy.io.wavfile
from scipy.fftpack import dct

# importing all the dependencies
import pandas as pd # data frame
import numpy as np # matrix math
from glob import glob # file handling
import librosa # audio manipulation
from sklearn.utils import shuffle # shuffling of data
import os # interation with the OS
from random import sample # random selection
from tqdm import tqdm

from modules.Utilities import Utilities

import skimage.measure # matrix boyu azaltiyor

# fixed param
PATH = '/home/ubuntu/Downloads/train/train/audio/'

def load_files(path):
	# write the complete file loading function here, this will return
	# a dataframe having files and labels
	# loading the files
	train_labels = os.listdir(PATH)
	train_labels.remove('_background_noise_')
	labels_to_keep = ['yes', 'no', 'up', 'down', 'left', 'right', 'on', 'off', 'stop', 'go', 'silence']
	train_file_labels = dict()
	for label in train_labels:
		files = os.listdir(PATH + '/' + label)
		for f in files:
			train_file_labels[label + '/' + f] = label

	train = pd.DataFrame.from_dict(train_file_labels, orient='index')
	train = train.reset_index(drop=False)
	train = train.rename(columns={'index': 'file', 0: 'folder'})
	train = train[['folder', 'file']]
	train = train.sort_values('file')
	train = train.reset_index(drop=True)

	def remove_label_from_file(label, fname):
		return path + label + '/' + fname[len(label)+1:]

	train['file'] = train.apply(lambda x: remove_label_from_file(*x), axis=1)
	train['label'] = train['folder'].apply(lambda x: x if x in labels_to_keep else 'unknown')

	labels_to_keep.append('unknown')

	return train, labels_to_keep


# we now convert it to spertogram
# goto: https://www.kaggle.com/davids1992/data-visualization-and-investigation
def log_specgram(audio, sample_rate, window_size=10,  step_size=10, eps=1e-10):
    nperseg = int(round(window_size * sample_rate / 1e3))
    noverlap = int(round(step_size * sample_rate / 1e3))
    #print(nperseg)
    #print(noverlap)
    a, b, spec = scipy.signal.spectrogram(audio,
                                    fs=sample_rate,
                                    window='hann',
                                    nperseg=nperseg,
                                    noverlap=noverlap,
                                    detrend=False)
    x=np.log(spec.T.astype(np.float32) + eps)
    #return x[:-1,]-x[1:,]
    return x

# train, labels_to_keep = load_files(PATH)
#
# # making word2id dict
# word2id = dict((c,i) for i,c in enumerate(sorted(labels_to_keep)))
#
# # get some files which will be labeled as unknown
# unk_files = train.loc[train['label'] == 'unknown']['file'].values
# unk_files = sample(list(unk_files), 1000)
#
#
#
# print(word2id)


train_audio_path = PATH
filename = '/tree/24ed94ab_nohash_0.wav' # --> 'Yes'
#filename = '/tree/1a073312_nohash_0.wav'
sample_rate, audio = scipy.io.wavfile.read(str(train_audio_path) + filename)


plt.figure(figsize = (15, 4))
plt.plot(audio)
plt.show()

u = Utilities()
#u.playSound(str(train_audio_path) + filename)


# goto: https://medium.com/@ageitgey/machine-learning-is-fun-part-6-how-to-do-speech-recognition-with-deep-learning-28293c162f7a
# We convert it into chunks of 20ms each i.e. units of 320
audio_chunks = []
n_chunks = int(audio.shape[0]/320)
for i in range(n_chunks):
    chunk = audio[i*320: (i+1)*320]
    audio_chunks.append(chunk)
audio_chunk = np.array(audio_chunks)



spectrogram= log_specgram(audio, sample_rate, 10, 3)
spec = spectrogram.T
print(spec.shape)
plt.figure(figsize = (15,4))
plt.imshow(spec, aspect='auto', origin='lower')
plt.show()
