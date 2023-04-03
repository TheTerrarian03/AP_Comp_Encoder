import numpy as np
import wavio
from matplotlib import pyplot as plt 
import math
import random
import library


def read_file_get_sampwidth(file_name: str):
    file_data = wavio.read(file_name)
    return file_data.sampwidth

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
    print(file_data.sampwidth)
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

def get_most_common_num(num_list: list):
    return max(set(num_list), key=num_list.count)

abs_diff = lambda base, val : 0

def abs_diff(base, val):
    return 

def parse_for_all(sound_data: np.array, sample_rate: float):
    TRACK = 0

    get_val = lambda i : sound_data[i][TRACK]
    
    frequencies = []
    samples_per_period = 0
    tracking_samples = False

    for i in range(1, len(sound_data)):
        # print(get_val(i))

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

def parse_by_time(sound_data: np.array, sample_rate: float, note_time: float):
    TRACK = 0
    MAX_CYCLE_DETECTS = 4

    get_val = lambda i : sound_data[i][TRACK]
    
    frequencies = []

    # get max samples given sample rate and note time
    MAX_CYCLE_SAMPLES = sample_rate * note_time
    MAX_NOTES = round((len(sound_data) / MAX_CYCLE_SAMPLES), 0)
    # get list of starting positions for each note
    starting_indexes = []
    for i in range(int(MAX_NOTES)):
        new_index = float(i) * MAX_CYCLE_SAMPLES
        new_index = round(new_index, 0)
        new_index += 1
        starting_indexes.append(new_index)
    print(f"max cycle samples: " + str(MAX_CYCLE_SAMPLES) + ", max notes: " + str(MAX_NOTES) + ", starting indexes: " + str(starting_indexes))
    # for each starting index
    for start_index in starting_indexes:
        # for range of starting to starting+max
        current_freqs = []
        samples_per_period = 0
        tracking_samples = False
        for i in range(int(MAX_CYCLE_SAMPLES)-3):
            sub_index = int(i + start_index)
            # print("sub index", sub_index, "type", type(sub_index))
            # print("start index:", start_index, ",i:", i, ", sub index:", sub_index)
            # look for frequencies
            # if wave goes above 0, cycle completed or started
            if get_val(sub_index-1) < 0 and get_val(sub_index) >= 0:
                # if we're not already tracking, start tracking and set samples to 0 based on current value
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
                    if (len(current_freqs) > 0):
                        if (current_freqs[-1] != closest_frequency):
                            current_freqs.append((closest_frequency))
                    else:
                        current_freqs.append(closest_frequency)
                    
                    # reset tracking
                    samples_per_period = 0
                    tracking_samples = False

                    # print("tracking samples, calculating")
                
            if (tracking_samples):
                samples_per_period += 1
            
            # when list len > max cycle detects
                # quit / break
            if (len(current_freqs) > MAX_CYCLE_DETECTS):
                break
        # at end:
            # calc freq and add to total list
        print(current_freqs)
        frequencies.append(get_most_common_num(current_freqs))
        # frequencies.append(closest_num(np.average(current_freqs), library.all_frequencies))
    
    # return total list
    return frequencies

def get_note_length(sound_data: np.array, doRound: bool=True):
    TRACK = 0
    last_point = sound_data[-1][TRACK]
    samp_widths = [8, 16, 24, 32]
    width_to_1_mult = 2/(2**samp_widths[read_file_get_sampwidth("test.wav")-1])
    scaled_point = last_point * width_to_1_mult
    if (doRound):
        scaled_point = round(scaled_point, 3)
    return scaled_point

def decode(sound_data: np.array, sample_rate: float):
    # get all frequencies
    # determine note length
    # parse for 
    # all_frequencies = parse_for_all(sound_data, sample_rate)
    # print(all_frequencies)
    note_length = get_note_length(sound_data)
    frequencies = parse_by_time(sound_data, sample_rate, note_length)
    print(frequencies)


if __name__ == "__main__":
    sound_data = read_file_get_data("test.wav")
    sample_rate = read_file_get_rate("test.wav")
    note_length = get_note_length(sound_data)
    
    decode(sound_data, sample_rate)
    # sampwidths = [8, 16, 24, 32]
    # print(read_file_get_sampwidth("test.wav"), sampwidths[read_file_get_sampwidth("test.wav")-1], (2**sampwidths[read_file_get_sampwidth("test.wav")-1])/2)
    # determine_note_length(sound_data, sample_rate)
