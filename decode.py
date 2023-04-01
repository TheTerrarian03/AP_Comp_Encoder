import numpy as np
import wavio
from matplotlib import pyplot as plt 
import math
import random
import library


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

def closest_num(num, num_list):
    """
    Given a number and a list of numbers, returns the number from the list
    that is closest to the given number.
    """
    closest = None
    diff = float('inf')  # Initialize with a very large number
    
    for n in num_list:
        if abs(num - n) < diff:
            diff = abs(num - n)
            closest = n
    
    return closest

def parse_for_all(sound_data: np.array, sample_rate: float):
    TRACK = 0

    get_val = lambda i : sound_data[i][TRACK]
    
    frequencies = []
    samples_per_period = 0
    tracking_samples = False

    for i in range(1, len(sound_data)):
        # if wave goes above 0, cycle completed or started
        if get_val(i-1) < 0 and get_val(i) >= 0:
            # if we're not alread y tracking, start tracking and set samples to 0 based on current value
            if (not tracking_samples):
                tracking_samples = True
                samples_per_period = 0

            # tracking samples, calculate frequency and restart
            else:
                # calculate frequency
                time_period = samples_per_period / sample_rate
                frequency = 1 / time_period

                closest_frequency = closest_num(frequency, library.all_frequencies)
                # print(closest_frequency)
                # add to list
                if (len(frequencies) > 0):
                    if (frequencies[-1] != closest_frequency):
                        frequencies.append((closest_frequency))
                else:
                    frequencies.append(closest_frequency)
                
                # reset tracking
                samples_per_period = 0
                tracking_samples = False

                # print("tracking samples, calculating")
            
        if (tracking_samples):
            samples_per_period += 1

    # print(samples_per_period, tracking_samples)
    return frequencies

def parse_by_time(sound_data: np.array, sample_rate: float):
    TRACK = 0

    get_val = lambda i : sound_data[i][TRACK]
    
    frequencies = []
    samples_per_period = 0
    tracking_samples = False

    for i in range(1, len(sound_data)):
        # if wave goes above 0, cycle completed or started
        if get_val(i-1) < 0 and get_val(i) >= 0:
            # if we're not alread y tracking, start tracking and set samples to 0 based on current value
            if (not tracking_samples):
                tracking_samples = True
                samples_per_period = 0

            # tracking samples, calculate frequency and restart
            else:
                # calculate frequency
                time_period = samples_per_period / sample_rate
                frequency = 1 / time_period

                closest_frequency = closest_num(frequency, library.all_frequencies)
                # print(closest_frequency)
                # add to list
                if (len(frequencies) > 0):
                    if (frequencies[-1] != closest_frequency):
                        frequencies.append((closest_frequency))
                else:
                    frequencies.append(closest_frequency)
                
                # reset tracking
                samples_per_period = 0
                tracking_samples = False

                # print("tracking samples, calculating")
            
        if (tracking_samples):
            samples_per_period += 1

    # print(samples_per_period, tracking_samples)
    return frequencies

def determine_note_length(sound_data: np.array, sample_rate: float):
    TRACK = 0
    song_len = len(sound_data) / sample_rate

def decode(sound_data: np.array, sample_rate: float):
    # get all frequencies
    # determine note length
    # parse for 
    all_frequencies = parse_for_all_frequencies(sound_data, sample_rate)
    print(all_frequencies)


if __name__ == "__main__":
    sound_data = read_file_get_data("test.wav")
    sample_rate = read_file_get_rate("test.wav")
    
    decode(sound_data, sample_rate)
    # determine_note_length(sound_data, sample_rate)
