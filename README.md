# Computer-Sound-and-Music
# Audio System Interaction

## Description
This program generates a 500Hz sine wave and a hard-clipped version of that wave to simulate a "symmetrical diode hard clip" distortion effect. It writes these to WAV files and plays the distorted version directly to the system audio.

## How it Went
- **Challenges:** (Example: Finding the correct path for the WAV files or configuring the sounddevice library).
- **Results:** The clipping is clearly visible at 1/4 maximum amplitude when viewed in Audacity.

## What is Still to be Done
- (Example: Adding a UI for frequency selection or implementing other distortion types like soft clipping).

## Build and Run Instructions
1. Ensure you have Python 3.12+ installed.
2. Install dependencies:
   ```bash
   pip install numpy scipy sounddevice
   
