import numpy as np

class Audio:
    def __init__(self):
        pass
    def write_sine_wave_file(self, morse_string):
        """This Method takes the morse string. Splits it out and creates chunks based on their audio equivalent.
        It combines the chunks and returns the value to be saved to an audio file.

        destination format:
            bit-depth = 16bit
            sample rate = 44100

        Returned composite is assumed to use the scipy.io.wavfile write function to save to local disc.
        """
        length = {
            # one unit
            ".": .05,
            # dash = 3 units
            "-": .15,
            # letter space = 3 units
            " ": .15,
            # word space = 7 units = 'space' + .2 + 'space' (.6 on either side + .2)
            "/": .05
        }
        samplerate = 44100
        fs = 1000

        def create_file_chunk(character):
            t = np.arange(samplerate * length[character]) / samplerate
            amplitude_on = np.iinfo(np.int16).max
            if character == "/" or character == " ":
                return np.sin(2 * np.pi * t * fs)
            else:
                return amplitude_on * np.sin(2 * np.pi * t * fs)


        chunks= []
        for x in list(morse_string):
            chunks.append(create_file_chunk(x))
            chunks.append(create_file_chunk(" "))

        return {
            "data" : np.concatenate(chunks).astype(np.int16),
            "sample_rate": samplerate,
            "num_channels": 1,
            }


