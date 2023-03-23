import numpy as np
import wavio
from matplotlib import pyplot as plt 
import math


# # have user enter in some ascii text
# user_input = input("enter some text:\n$ ")

# for char in user_input:
#     print(f"char: {char} ; int: {ord(char)}")

rate = 22050           # samples per second
T = 3                  # sample duration (seconds)
n = int(rate*T)        # number of samples
t = np.arange(n)/rate  # grid of time values

afreq = 440.0          # sound frequency (Hz)
gfreq = 392.0

def make_piano_wave(base_freq, rate, time_cap):
    wave_values = []
    calc_val = lambda t : math.sin(2 * math.pi * base_freq * t) * math.exp(-0.0004 * 2 * math.pi * base_freq * t)

    for time in range(time_cap*rate):
        print(time, calc_val(time))
        wave_values.append(calc_val(time))
    
    return np.array(wave_values)

sin_a = np.sin(2*np.pi * afreq * t)
sin_g = np.sin(2*np.pi * gfreq * t)
piano_440 = make_piano_wave(800, rate, 1)

combined = np.concatenate((sin_a[0:rate], sin_g[0:rate]))

# for value in combined:
#     print(value)

plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(sin_a[:200])
plt.plot(sin_g[:200])
plt.show()

# wavio.write("sine24.wav", combined, rate, sampwidth=3)