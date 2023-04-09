import numpy as np
import wavio
from matplotlib import pyplot as plt 
import math
import random
import library


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

def sine(hz: float, sample_rate: int, max_time: float, decay: float=0, is_np_array: bool=True):
    """Takes in some parameters and generates an array containing values over time that make up the sound wave
    
        Parameters:
            hz (float): frequency of the wave
            sample_rate (int): amount of samples per second the output file will have
            max_time (float): max length of time the note can sound for
            decay (float): how much to scale sound wave by over time
            is_np_array (bool): whether or not to convert to a numpy array
    """

    # function to calculate value at given time
    def calc_val(curr_time):
        t = curr_time * hz # get time scaled by frequency
        t *= (2 * math.pi)/sample_rate  # scale to sample rate

        curr_val = math.sin(t)  # sine value at time
        curr_val *= 1-(decay * curr_time/sample_rate)  # apply decay

        return curr_val  # return value
    
    # define a list to hold values of wave
    wave_values = []

    # calculate and append values for wave for its entire duration
    for time in range(int(max_time * sample_rate)):
        wave_values.append(calc_val(time))
    
    # convert to numpy array if needed and return array
    if is_np_array:
        return np.array(wave_values)
    else:
        return wave_values

def scale_to_1(np_array: np.array):
    """
    Takes in a numpy array and scales each value down to a max rangeof -1 to 1
    
        Parameters
            np_array (np.array): the numpy array to scale
    """

    # define max and min values
    max_val = 0
    min_val = 0

    # for each value in the numpy array, adjust max and min values as needed
    for val in np_array:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
    
    # define a new array of the original, but scaled down to 1
    scaled_array = np_array / max(max_val, -min_val)
            
    # return said array
    return scaled_array

def cap_at_1(np_array: np.array):
    """
    Takes in a numpy array and caps each value at either -1 or 1
    
        Parameters
            np_array (np.array): the numpy array to cap
    """

    # define a new array containing capped values
    capped_array = []

    # for each value in the array, cap at -1 to 1
    for val in np_array:
        if val > 1:
            val = 1
        if val < -1:
            val = -1
        
        # add to array
        capped_array.append(val)
    
    # return a 1D numpy version of that array
    return np.array(capped_array)

def make_waves(frequencies: list, sample_rate: int, note_time: float, decay: float=0, show_graph: bool=False) -> np.array:
    """
    Takes in a list of frequencies for notes, and converts them to a (very large) array of data, representing sound waves
    
        Parameters
            frequencies (list): list of note frequencies to write out, one after another
            sample_rate (int): sample rate of target .wav file
            note_time (float): how long (in seconds) each note should play for (0.x - 1 seconds)
            decay (float): scale of note volume per 1 second
            show_graph (boolean): whether to show a pyplot graph of waves
    """

    # define a total list to hold all of the note values for the whole thing
    total_list = []

    # append to the total list, the wave needed for each note
    for note_freq in frequencies:
        note_data_list = sine(note_freq, sample_rate, note_time, decay=decay, is_np_array=False)
        total_list = np.concatenate([total_list, note_data_list])

    # cap note time within 0 and 1
    capped_note_time = max(0, min(note_time, 1))

    # scale array
    scaled_array = scale_to_1(total_list)
    # append at the very end, a single value which holds the note time/length
    scaled_array = np.append(scaled_array, np.array([capped_note_time]))

    # setup and show graph if enabled
    if(show_graph):
        plt.title("Sound - graphed!")
        plt.xlabel("x axis - time") 
        plt.ylabel("y axis - amplitude")
        plt.plot(scaled_array)
        plt.show()

    # return the array containing the final wave
    return scaled_array


if __name__ == "__main__":
    ### example usage of making wave and writing file

    # define sample rate
    SAMPLE_RATE = 88200

    # define frequency list
    # freq_list = library.all_frequencies
    freq_list = [440, 1760, 3520, 246.9, 493.9, 261.6, 523.3, 587.3, 1175, 659.3, 1319, 349.2, 698.5, 1568, 3136]
    
    # make wave data
    wave_data = make_waves(freq_list, SAMPLE_RATE, 0.15, show_graph=False)
    
    # write file
    write_file("test.wav", wave_data, SAMPLE_RATE, sample_width=2)
