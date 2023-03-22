import numpy as np
import wavio


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

sin_a = np.sin(2*np.pi * afreq * t)
sin_g = np.sin(2*np.pi * gfreq * t)

combined = np.concatenate((sin_a[0:rate], sin_g[0:rate]))

for value in combined:
    print(value)

wavio.write("sine24.wav", combined, rate, sampwidth=3)