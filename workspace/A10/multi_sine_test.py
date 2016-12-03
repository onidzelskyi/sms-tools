import sys
import os

import numpy as np
from scipy.signal import get_window

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), '../software/models'))

import utilFunctions as UF
from sineModel import sineModelMultiRes, sineModel

# http://www.freesound.org/people/dshoot85/sounds/331025/
input_file1 = './A10/input1.wav'
(fs, x1) = UF.wavread(os.path.join(os.path.dirname(os.getcwd()), input_file1))

# http://www.freesound.org/people/cedar_ren/sounds/331007/
input_file2 = './A10/input2.wav'
(fs, x2) = UF.wavread(os.path.join(os.path.dirname(os.getcwd()), input_file2))

# Band distribution
B1 = (0, 1000)
B2 = (1000, 5000)
B3 = (5000, 22050)

# Window sizes
M1 = 2035  # (6 * 44100 / 100)
M2 = 265  # (6 * 44100 / 1000)
M3 = 53  # (6 * 44100 / 5000)

# DFT frames
N1 = int(np.exp2(np.ceil(np.log2(M1))))
N2 = int(np.exp2(np.ceil(np.log2(M2))))
N3 = int(np.exp2(np.ceil(np.log2(M3))))

# Window types
window_type_1 = 'blackman'
window_type_2 = 'blackman'
window_type_3 = 'blackman'

w1 = get_window(window_type_1, M1)
w2 = get_window(window_type_2, M2)
w3 = get_window(window_type_3, M3)

# Analysis
W = [w1, w2, w3]
N = [N1, N2, N3]
t = -120
B = [B1, B2, B3]
y1 = sineModelMultiRes(x1, fs, W, N, t, B)
y2 = sineModelMultiRes(x2, fs, W, N, t, B)

# Write
UF.wavwrite(y1, fs, 'A10-b-1.wav')
UF.wavwrite(y2, fs, 'A10-b-2.wav')

