# STM32-DAQ-System
A Data Acquisition Module for audio processing using an STM32 microcontroller. Essentially functioning as a voice recorder, this project features real-time ADC value acquisition, conversion to WAV files using the RIFF format, and CLI-based control for recording and processing audio data


# Project Structure

MAIN_STM_CODE.c: The main firmware code for STM32, which includes ADC data acquisition, sensor interfacing, and UART communication.

Python Scripts

serial_disc.py: Handles serial communication with the STM32 board, records ADC values, and processes it.
moving_average.py: Provides a function for calculating simple moving averages.

WAV File Generation

wav_header.c: C code to generate a WAV file adhering to the RIFF format with the specified audio parameters.

CLI Interface:
menu.py script that provides user controlled options for data acquisition, processing, and playback.
