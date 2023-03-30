import numpy as np
import wavio
from matplotlib import pyplot as plt 
import math
import random


def read_file_get_data(file_name: str):
    """
    Takes in a file name and returns the sound wave data as an np array
    
        Parameters:
            file_name (str): a string, holding the name for the file to be written (e.x. "example.wav")
    """

    file_data = wavio.read(file_name)
    sound_data = file_data.data
    return sound_data

def read_file_get_rate(file_name: str):
    """
    Takes in a file name and returns the sample rate
    
        Parameters:
            file_name (str): a string, holding the name for the file to be written (e.x. "example.wav")
    """
    file_data = wavio.read(file_name)
    return file_data.rate

def parse_for_frequencies(sound_data: np.array, sample_rate: float):
    TRACK = 0

    get_val = lambda i : sound_data[i][TRACK]
    
    frequencies = []
    frequencies_to_average = []
    samples_per_period = 0

    for i in range(1, len(sound_data)):
        # if wave goes above 0, cycle completed
        if get_val(i-1) < 0 and get_val(i) >= 0:
            # is samples number more than 0?
            if (sample_rate > 0):
                # calculate frequency
                time_period = samples_per_period / sample_rate
                frequency = 1 / time_period

                # add to list
                if (len(frequencies) > 0):
                    if (frequencies[-1] != frequency):
                        frequencies_to_average.append(frequency)
                else:
                    frequencies_to_average.append(frequency)
            
            samples_per_period = 0

        samples_per_period += 1
        
        if (len(frequencies_to_average) > 10):
            avg_frequency = sum(frequencies_to_average) / len(frequencies_to_average)
            frequencies.append(avg_frequency)
            frequencies_to_average = []

        print(frequencies)
    
        
        # # check if values passed 0
        # if (last_val1 > 0) and (val < 0):
        #     times_passed_zero += 1
        # if (last_val2 < 0) and (val > 0):
        #     times_passed_zero += 1
        
        # # if times passed 0 is at 3, calculate frequency and append to list
        # if (times_passed_zero == 3):
        #     # append sample counter for now
        #     # note_freq = sample_rate / (samples_per_period / 2)
        #     note_freq = sample_rate * (1 / (samples_per_period / 2))
        #     # 22050*(1/(440/2))

        #     if (len(frequencies) > 0):
        #         if (frequencies[-1] != note_freq):
        #             frequencies.append(note_freq)
        #     else:
        #         frequencies.append(note_freq)

        #     print(f"PERIOD FOUND! SPP: {samples_per_period}, HZ: {note_freq}")
        #     # reset counting
        #     times_passed_zero = 0
        #     samples_per_period = 0

        # # else, if times passed 0 is more than 0 (counting started), increment sample counter
        # elif (times_passed_zero > 0):
        #     samples_per_period += 1
        
        # # debugging, print last and current val
        # print(f"Last: {last_val1}, Current: {val}, TP0: {times_passed_zero}, SPP: {samples_per_period}")
        
        # # update last value
        # last_val1 = last_val2
        # last_val2 = val

        # print(frequencies)


if __name__ == "__main__":
    sound_data = read_file_get_data("test.wav")
    sample_rate = read_file_get_rate("test.wav")
    
    parse_for_frequencies(sound_data, sample_rate)
    
