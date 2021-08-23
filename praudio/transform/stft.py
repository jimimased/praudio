"""
This module features a class that extracts Short-Time Fourier Transform
from signals.
"""

import librosa

from praudio.transform.transform import Transform
from praudio.io.signal import Signal


class STFT(Transform):
    """This class extracts a Short-Time Fourier transform from a signal.
    It's a concrete Transform. librosa facilities are used to extract STFT.

    Attributes:
        - frame_length: Length of the windowed signal after padding with zeros
        - hop_length: Number of audio samples between adjacent STFT columns
        - win_length: Each frame of audio is windowed by window of length
            win_length and then padded with zeros to match frame_length
        - window: Windowing method employed for STFT. Default is 'hann'

    Check librosa documentation at http://librosa.org/doc/main/generated/librosa.stft.html
    to learn more about attributes.
    """

    def __init__(self,
                 frame_length: int = 2048,
                 hop_length: int = 1024,
                 win_length: int = 2048,
                 window: str = "hann"):
        super().__init__("stft")
        self.frame_length = frame_length
        self.hop_length = hop_length
        self.win_length = win_length
        self.window = window

    def process(self, signal: Signal) -> Signal:
        """Extract complex STFT from waveform and modifies signal.

        :param signal: Signal object. Note: this transform works only with
            waveform data

        :return: signa: Modified signal
        """
        stft = librosa.stft(signal.data,
                            n_fft=self.frame_length,
                            hop_length=self.hop_length,
                            win_length=self.win_length,
                            window=self.window)
        signal.data = stft
        signal.name = self.name
        return signal
