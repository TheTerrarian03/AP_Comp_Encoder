import numpy as np
import wavio
from matplotlib import pyplot as plt 
import math
import random


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

def sine(base_freq, rate, time_cap):
    # def calc_val(curr_time):
        # return math.sin(2 * math.pi * time)

    wave_values = []
    # calc_val = lambda t : math.sin(2 * math.pi * t * base_freq)
    calc_val = lambda t : math.sin(((2*math.pi)/rate) * t * base_freq)

    for time in range(time_cap*rate):
        wave_values.append(calc_val(time))
    
    return np.array(wave_values)

def random_int(rate, amplitude, time_cap):
    wave_values = []

    for time in range(time_cap * rate):
        wave_values.append(random.randint(-1, 1) * amplitude)
    
    return np.array(wave_values)

sin_a = np.sin(2*np.pi * afreq * t)
# sin_g = np.sin(2*np.pi * gfreq * t)
sin_a2 = sine(afreq, rate, 1)
piano_440 = make_piano_wave(800, rate, 1)
random_ints = random_int(rate, 1, 1)

# combined = np.concatenate((sin_a[0:rate], sin_g[0:rate]))

# for value in combined:
#     print(value)

plt.title("Sound - graphed!")
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
# plt.plot(sin_a[:200])
plt.plot(sin_a2)
plt.plot(random_ints)
plt.show()

wavio.write("sine24.wav", random_ints, rate, sampwidth=3)