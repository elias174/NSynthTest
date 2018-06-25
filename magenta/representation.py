from IPython.display import Image, Audio
import librosa
import librosa.display

import matplotlib.pyplot as plt

import numpy as np


def show_example(filename):
    data, sr = librosa.load(filename, sr=16000, duration=2)
    specgram = librosa.stft(data)
    specgram = librosa.amplitude_to_db(specgram, ref=np.max)
    plt.figure(figsize=(15,10))
    librosa.display.specshow(specgram,
                             sr=sr,
                             x_axis='time',
                             y_axis='log')
    plt.title(filename + ' log magnitude spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.savefig('%s.svg' % filename)
    return Audio(data, rate=sr)


show_example('sounds/gen_395058__mustardplug__breakbeat-hiphop-a4-4bar-96bpm.wav')
show_example('sounds/395058__mustardplug__breakbeat-hiphop-a4-4bar-96bpm.wav')