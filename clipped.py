import numpy as np
from scipy.io import wavfile
import sounddevice as sd

SAMPLE_RATE = 48000  
DURATION = 1.0       
FREQUENCY = 500.0    
MAX_AMP = 32767      
QUARTER_AMP = 8192  
HALF_AMP = 16384  

def generate_audio():
    
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
    sine_data = QUARTER_AMP * np.sin(2 * np.pi * FREQUENCY * t)
    sine_data = sine_data.astype(np.int16)
    print("Writing sine.wav...")
    wavfile.write("sine.wav", SAMPLE_RATE, sine_data)
    clipped_data = HALF_AMP * np.sin(2 * np.pi * FREQUENCY * t)
    clipped_data = np.clip(clipped_data, -QUARTER_AMP, QUARTER_AMP)
    clipped_data = clipped_data.astype(np.int16)
    print("Writing clipped.wav...")
    wavfile.write("clipped.wav", SAMPLE_RATE, clipped_data)
    print(f"Playing clipped sine wave at {FREQUENCY}Hz...")
    sd.play(clipped_data, SAMPLE_RATE)
    sd.wait()
    print("Done!")

if __name__ == "__main__":
    generate_audio()