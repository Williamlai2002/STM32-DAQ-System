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


# Diagrams
A high level block diagram of the system:
<img width="732" alt="Screen Shot 2024-08-11 at 1 01 59 am" src="https://github.com/user-attachments/assets/dcb9d690-2156-4a75-8af7-02f3e15856ff">


A more detailed block diagram demonstrating system interaction:
<img width="739" alt="Screen Shot 2024-08-11 at 1 02 08 am" src="https://github.com/user-attachments/assets/6fd5f582-bf9c-4156-b48d-0b271d38b689">


# Outcome

This Data Acquisition Module for STM32 microcontrollers represents a robust solution for high-speed audio data processing and analysis. By achieving a sampling rate of 5000 S/s through the use of Direct Memory Access (DMA) and a ping pong buffer, it efficiently handles large volumes of audio data, making it suitable for various applications requiring precise and high-fidelity recordings.

The choice of a moving average filter system enhances data management by smoothing out noise and fluctuations, a crucial feature considering the low occurrence of extreme frequency components in typical audio signals. This design decision ensures that the recorded data remains clean and representative of the actual audio content.

With a recording duration that exceeds 60 seconds and the capability for early termination, users have the flexibility to capture extended audio segments or stop recordings as needed. The inclusion of graphical data visualization tools and CSV storage capabilities further facilitates in-depth analysis and interpretation of the recorded data.

Additionally, the system's support for multiple audio recordings ensures that users can retain and manage multiple datasets without overwriting previous recordings, enhancing data organization and usability.



