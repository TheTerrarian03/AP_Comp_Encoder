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

    print(sound_data)
    return sound_data


if __name__ == "__main__":
    sound_data = (read_file_get_data("bug.wav"))
    for val in sound_data:
        # [#] np.ndarray | # np.int16
        print(val, type(val), val[0], type(val[0]))
