import numpy as np
from scipy.io import wavfile

# Constants
FS = 48000
BAUD = 300
SAMPLES_PER_BIT = FS // BAUD  # 160
FREQ_SPACE = 2025
FREQ_MARK = 2225

def get_reference_waves(f, fs, n_samples):
    n = np.arange(n_samples)
    cos_ref = np.cos(2 * np.pi * f * n / fs)
    sin_ref = np.sin(2 * np.pi * f * n / fs)
    return cos_ref, sin_ref

# Pre-compute for both frequencies
space_cos, space_sin = get_reference_waves(FREQ_SPACE, FS, SAMPLES_PER_BIT)
mark_cos, mark_sin = get_reference_waves(FREQ_MARK, FS, SAMPLES_PER_BIT)


def get_power(block, cos_ref, sin_ref):
    
    i = np.dot(block, cos_ref)
    q = np.dot(block, sin_ref)
    return i**2 + q**2


def process_wav(filename):
    samplerate, data = wavfile.read(filename)
    # Convert to float -1.0 to 1.0
    samples = data.astype(np.float32) / 32768.0
    
    message = ""
    # Process in chunks of 10 bits
    for i in range(0, len(samples), SAMPLES_PER_BIT * 10):
        frame = samples[i : i + SAMPLES_PER_BIT * 10]
        if len(frame) < SAMPLES_PER_BIT * 10:
            break
            
        bits = []
        # Break the 10-bit frame into individual bits
        for b in range(10):
            bit_block = frame[b * SAMPLES_PER_BIT : (b + 1) * SAMPLES_PER_BIT]
            
            p_space = get_power(bit_block, space_cos, space_sin)
            p_mark = get_power(bit_block, mark_cos, mark_sin)
            bits.append(1 if p_mark > p_space else 0)
        
        byte_val = 0
        for idx, bit in enumerate(bits[1:9]):
            byte_val += bit * (2 ** idx)
            
        message += chr(byte_val)
    
    return message

if __name__ == "__main__":
    import os
    
    filename = 'message.wav'
    
    if not os.path.exists(filename):
        print(f"Error: Could not find {filename} in the current folder!")
    else:
        print("Processing...")
        decoded_text = process_wav(filename)
        print("\n--- DECODED MESSAGE ---")
        print(decoded_text)
        print("-----------------------")