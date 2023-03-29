import numpy as np
import wavio
from matplotlib import pyplot as plt 
import math
import random


def write_file(file_name: str, data_array: np.array, sample_rate: int=44100, sample_width: int=2):
    """
    Takes in a file name and list of data, and writes it out to a .wav file for listening or sharing (or decoding)

        Parameters
            file_name (str): a string, holding the name for the file to be written (e.x. "example.wav")
            data_array (np.array): a 1D or 2D np array holding all the data to be written
            sample_rate (int): how many samples per second are there? Default: 44,100
            sample_width (int): size, 1-4, of wav file data. Default: 2 (16 bits)
    """

    wavio.write(file_name, data_array, sample_rate, sampwidth=sample_width)

def sine(hz: float, sample_rate: int, max_time: float, decay: float=0, isNpArray: bool=True):
    def calc_val(curr_time):
        t = curr_time * hz # get time scaled by frequency
        t *= (2 * math.pi)/sample_rate  # scale to sample rate

        curr_val = math.sin(t)  # sine value at time
        curr_val *= 1-(decay * curr_time/sample_rate)

        return curr_val
    
    wave_values = []
    for time in range(int(max_time * sample_rate)):
        wave_values.append(calc_val(time))
    
    if isNpArray:
        return np.array(wave_values)
    else:
        return wave_values

def scale_to_1(np_array: np.array):
    max_val = 0
    min_val = 0

    for val in np_array:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
    
    scaled_array = np_array / max(max_val, -min_val)
            
    return scaled_array

def cap_at_1(np_array: np.array):
    capped_array = []

    for val in np_array:
        if val > 1:
            val = 1
        if val < -1:
            val = -1
        
        capped_array.append(val)
    
    return np.array(capped_array)

def make_waves(frequencies: list, sample_rate: int, note_time: float, decay: float=0, show_graph: bool=False) -> np.array:
    """
    Takes in a list of frequencies for notes, and converts them to a (very large) array of data, representing sound waves
    
        Parameters
            frequencies (list): list of note frequencies to write out, one after another
            sample_rate (int): sample rate of target .wav file
            note_time (float): how long (in seconds) each note should play for
            decay (float): scale of note volume per 1 second
            show_graph (boolean): whether to show a pyplot graph of waves
    """

    total_list = []

    for note_freq in frequencies:
        note_data_list = sine(note_freq, sample_rate, note_time, decay=1, isNpArray=False)
        total_list = np.concatenate([total_list, note_data_list])

    print(total_list)
    scaled_array = scale_to_1(total_list)

    if(show_graph):
        plt.title("Sound - graphed!")
        plt.xlabel("x axis - time") 
        plt.ylabel("y axis - amplitude") 
        # plt.plot(sin_a[:200])
        plt.plot(scaled_array)
        plt.show()

    return scaled_array


if __name__ == "__main__":
    frequencies = [random.randrange(98, 650) for x in range(100)]
    print(frequencies)
    # wave_data = make_waves([261.6, 293.7, 329.6, 349.2, 392, 349.2, 329.6, 293.7, 261.6], 44100, 0.25, decay=1)
    wave_data = make_waves(frequencies, 44100, 0.025, decay=0.025)
    # wavio.write("bug.wav", wave_data, 44100, sampwidth=3)
    write_file("bug.wav", wave_data)
