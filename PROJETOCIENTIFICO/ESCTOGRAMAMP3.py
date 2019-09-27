import matplotlib.pyplot as plt
import scikits.audiolab as audiolab
sound = audiolab.sndfile('Violin_for_spectogram.ogg', 'read')
y = sound.read_frames(sound.get_nframes())
Pxx, freqs, bins, im = plt.specgram (y , NFFT = 512 , Fs = 44100)
plt.xlim(0, len(y)/44100.0)
plt.ylim(0, 22050.0)
plt.colorbar(im).set_label(u'Intensidad (dB')
plt.xlabel(u'Tiempo(s')
plt.ylabel(u'Frecuencia(Hz)')