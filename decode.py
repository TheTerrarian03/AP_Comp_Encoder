import numpy as np
import wavio
from matplotlib import pyplot as plt 
import math
import random
import library


def read_file_get_sampwidth(file_name: str):
    """
    Takes in a file name and returns the sample width of the file
    
        Parameters:
            file_name (str): a string, holding the name for the file to be written (e.x. "example.wav")
    """

    # get data then return sample width value from data
    return wavio.read(file_name).sampwidth

def read_file_get_data(file_name: str):
    """
    Takes in a file name and returns the sound wave data as an np array
    
        Parameters:
            file_name (str): a string, holding the name for the file to be written (e.x. "example.wav")
    """

    # get file data then return sound data value
    return wavio.read(file_name).data

def read_file_get_rate(file_name: str):
    """
    Takes in a file name and returns the sample rate
    
        Parameters:
            file_name (str): a string, holding the name for the file to be written (e.x. "example.wav")
    """

    # get file data then return rate of file
    return wavio.read(file_name).rate

def closest_num(num, num_list):
    """
    Given a number and a list of numbers, returns the number from the list
    that is closest to the given number.
    (Written by ChatGPT)
    """
    closest = None
    diff = float('inf')  # Initialize with a very large number
    
    for n in num_list:
        if abs(num - n) < diff:
            diff = abs(num - n)
            closest = n
    
    return closest

def get_most_common_num(num_list: list):
    """
    Small function for returning the most common number from a list
    (stolen from the internet :D )
    """
    return max(set(num_list), key=num_list.count)

def parse_by_time(sound_data: np.array, sample_rate: int, note_time: float):
    """
    Takes in some sound and file data, then finds all frequencies in the 'song' at each note spot
    
        Parameters:
            sound_data (np.array): the numpy array that holds all of the wave data for the song
            sample_rate (int): the number of samples per second the input file has
            note_time (float): how long (in seconds) each note should be - CRUCIAL
    """

    # define some constants
    TRACK = 0
    MAX_CYCLE_DETECTS = 4

    # a lambda for getting the value at a certain index, here to compensate for tracks in .wav files
    get_val = lambda i : sound_data[i][TRACK]
    
    # define a list to hold all final frequencies to return
    frequencies = []

    # get max sample and note amounts, given sample rate and note time
    MAX_CYCLE_SAMPLES = sample_rate * note_time
    MAX_NOTES = round((len(sound_data) / MAX_CYCLE_SAMPLES), 0)

    # define and fill a list of starting positions for each note
    starting_indexes = []
    for i in range(int(MAX_NOTES)):
        new_index = float(i) * MAX_CYCLE_SAMPLES
        new_index = round(new_index, 0)
        new_index += 1
        starting_indexes.append(new_index)

    # for each starting index, find go for a while and find some frequencies
    for start_index in starting_indexes:
        # define variables to hold important information
        current_freqs = []  # current frequencies found
        samples_per_period = 0  # how many samples per period/cycle so far
        tracking_samples = False  # whether or not to track samples currently

        # for indexes in range of the starting index -> starting index + (max - 3), look for frequencies
        for i in range(int(MAX_CYCLE_SAMPLES)-3):
            # make a "sub index"- accounts for starting index
            sub_index = int(i + start_index)

            # if wave goes above 0, cycle either completed or started
            if get_val(sub_index-1) < 0 and get_val(sub_index) >= 0:
                # if we're not already tracking, cycle started, start tracking and set samples to 0
                if (not tracking_samples):
                    tracking_samples = True
                    samples_per_period = 0

                # we're tracking samples, cycle complete, calculate frequency and restart
                else:
                    # calculate frequency
                    time_period = samples_per_period / sample_rate
                    frequency = 1 / time_period

                    # get closest frequency
                    closest_frequency = closest_num(frequency, library.all_frequencies)

                    # add to list if not already there
                    if (len(current_freqs) > 0):
                        if (current_freqs[-1] != closest_frequency):
                            current_freqs.append((closest_frequency))
                    else:
                        current_freqs.append(closest_frequency)
                    
                    # reset tracking
                    samples_per_period = 0
                    tracking_samples = False

            # increment samples if tracking                
            if (tracking_samples):
                samples_per_period += 1
            
            # when list len > max cycle detects, break
            if (len(current_freqs) > MAX_CYCLE_DETECTS):
                break

        # at end, calc freq and add to total list
        frequencies.append(get_most_common_num(current_freqs))
    
    # return final list
    return frequencies

def get_note_length(sound_data: np.array, sample_width: int, do_round: bool=True):
    """
    Takes in some sound data and returns the intended time for each note
    
        Parameters
            sound_data (np.array): array of sound wave data
            sample_width (int): sample width of input file
            doRound (bool): whether or not to round to 3 decimal places
    """

    # define which track to look at
    TRACK = 0
    SAMP_WIDTHS = [8, 16, 24, 32]
    
    # get last point
    last_point = sound_data[-1][TRACK]
    
    # calculate scale from x-bit integer down to float
    width_to_1_mult = 2/(2**SAMP_WIDTHS[sample_width-1])

    # scale point
    scaled_point = last_point * width_to_1_mult

    # round if necessary
    if (do_round):
        scaled_point = round(scaled_point, 3)
    
    # return value
    return scaled_point

def decode(file_name: str):
    """
    DECODER! Takes in file name and does it all from here. Returns a list of frequencies
    
        Parameters
            file_name (str): Name of file to decode
    """

    sound_data = read_file_get_data(file_name)
    sample_rate = read_file_get_rate(file_name)
    sample_width = read_file_get_sampwidth(file_name)
    note_length = get_note_length(sound_data, sample_width, do_round=True)

    parsed_frequencies = parse_by_time(sound_data, sample_rate, note_length)
    return parsed_frequencies

if __name__ == "__main__":
    decode("test.wav")
