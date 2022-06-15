import scipy.io.wavfile
import numpy
import os


with open(os.path.abspath(f'static/audios/test.wav'), 'rb') as f:
    print(type(f.read()))
    response = f.read()
    a=bytearray(response)
    b = numpy.array(a, dtype=numpy.int16)

    scipy.io.wavfile.write(r'static/audios/test.wav', b)