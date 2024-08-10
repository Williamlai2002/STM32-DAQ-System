# libraries
import serial_disc
import time
import matplotlib.pyplot as plt
import pandas as pd
import serial_sensor
import pygame

def play_recording():
    #plays the audio file
    #no input
    #sound output

    pygame.init()   #initialises pygame
    pygame.mixer.init() # initilises the module that handles sounds

    try:
        #plays the sound
        recording = pygame.mixer.Sound("ADC_Week7/output.wav")
        recording.play()

    finally:
        #quits when sound is finished playing
        if pygame.mixer.get_busy() != True:
            pygame.mixer.quit()
            pygame.quit()



def record():
    #Records data from the serial and integrates a stop method using keyboard interrupt
    #Input:None
    #Output: Record data and stores it into file
    start_time = time.time()
    try:
         serial_disc.main()
    except KeyboardInterrupt:
        pass
    duration = time.time() - start_time
    data = open("ADC_Week7/adc_data.data")
    sum = 0
    while data.readline():
        sum += 1
    rate = sum/duration
    data.close()    
        
    print("========\nRecording finished\n=========")
    print(f"Duration: {duration}\nSample Rate: {rate}")
    print("Press enter to return")
    input("")
    
def show_plot(directory):
    #Shows the previously plotted recording data
    #input: none
    #output: Opens up the image

    #gets data using pandas
    with open(directory,"r") as data:

        #Set data and time list to plot
        dataPoints =[]
        time = []

        #append to list
        lines = data.readline()
        #as long as there are still lines to read
        while lines:
            lines = lines.strip().split(",")
            dataPoints.append(float(lines[0]))
            time.append(float(lines[1]))
            lines = data.readline()

    #plot
    plt.plot(time, dataPoints)
    plt.xlabel('Time (s)')
    plt.ylabel('ADC input')
    plt.title('ADC input vs Time')
    plt.show()
    
    #Show return directions
    print("Press enter to return")
    input("")


def main_screen():
    #Displays options
    #input: none
    #output: Displays options in terminal
    print("Audio Recording System")
    print("=======================")
    print("1. Record")
    print("2. Show Previous Plot")
    print("3. Playback")
    print("4. Quit")

if __name__ == '__main__':
    while True:
        main_screen()
        command = int(input("Enter command: "))
        if command == 1:
            print("=============\nInterrupt Option\n=============")
            print("1. Only user interrupt")
            print("2. User Interrupt and Sensor interrupt")
            mode = int(input("Choose option: "))
            if mode == 1:
                record()
            elif mode == 2:
                print("=============\nDistance\n=============")
                mini = int(input("Input needed proximity in mm to begin recording (default 100): "))
                serial_sensor.main(mini)
                record()
        elif command == 2:
            #shows options for plotting
            print("===============\nPlot Options\n===============")
            print("1. Raw Data")
            print("2. Filtered Data")
            #Get input
            type = int(input("Enter Option:"))

            if type == 1:
                show_plot("ADC_Week7/adc_data.csv") #plot to raw data
            elif type == 2:
                show_plot("ADC_Week7/adc_data_filtered.csv") #plot to filtered data
        elif command == 3:
            play_recording()
            #Show return directions
            print("Press enter to return")
            input("")
    
