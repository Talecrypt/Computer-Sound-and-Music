# Bell 103 Modem Demodulator
**Author:** Saif Abu Hananah

## Project Description
This project implements a demodulator for the Bell 103 modem protocol, specifically targeting the 300-baud "8N1" format. The program processes a 48kHz mono WAV file containing Frequency Shift Keying (FSK) signals and converts them back into ASCII text.

## Technical Implementation
- **FSK Detection:** Instead of a simple zero-crossing detector, this implementation uses I/Q correlation. For each 160-sample bit block, the signal is correlated with reference sine and cosine waves for the Space (2025 Hz) and Mark (2225 Hz) frequencies.
- **Optimization:** To ensure efficiency in Python, the inner loops were replaced with `numpy.dot` operations. This utilizes optimized C-libraries for the multiplication and summation of sample blocks against precomputed reference arrays.
- **Framing:** The decoder processes 10-bit frames (1 start bit, 8 data bits, 1 stop bit). It identifies the data bits and reconstructs the character byte using LSB-first bit ordering.

## Project Reflection
- **How it went:** The core logic of the detector was straightforward once the I/Q correlation concept was understood. Using NumPy significantly improved the processing speed compared to a standard loop.
- **Challenges:** The primary hurdle was ensuring the bit order (LSB-first) was handled correctly to avoid "scrambled" output.
- **Future Improvements:** Adding clock recovery or synchronization would make the modem more robust to timing drift or lead-in silence.