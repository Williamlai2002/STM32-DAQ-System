import serial
import serial.tools.list_ports
import time
import matplotlib.pyplot as plt
import os
from moving_average import simple_moving_average


def find_stm32_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "STM" in port.description:
            stm32_port = port.device
            return stm32_port
    return None

def poll_port(serial_port):
    try:
        ser = serial.Serial(serial_port, baudrate=2000000, timeout=0.01)
        data_points = []
        times = []
        start_time = time.time()

        # Ensure the ADC_vals directory exists
        output_directory = ""
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        # Path for the output file and graph
        output_file_path = os.path.join(output_directory, 'adc_data.DATA')
        output_file_pathraw = os.path.join(output_directory, 'adc_data.csv')
        output_file_pathfiltered = os.path.join(output_directory, 'adc_data_filtered.csv')
        
        output_graph_path = os.path.join(output_directory, 'adc_graph.png')

        # Open a file in the output directory to save the data
        with open(output_file_pathraw, 'w') as data_fileraw:
            buffer = ''
            while True:
                raw_data = ser.read(100000)  # Read data from the serial port
                data = raw_data.decode('utf-8', errors='ignore')  # Decode bytes to string
                buffer += data  # Append new data to buffer

                if '\n' in buffer:  # Check if complete lines are in the buffer
                    complete_data, buffer = buffer.rsplit('\n', 1)  # Split on the last newline, keeping the remainder
                    for line in complete_data.split('\n'):  # Process each complete line
                        if 'Time:' in line:
                            parts = line.split('Time:')  # Split line at 'Time:'
                            adc_value = parts[0].strip().split(' ')[1].strip(',') # Extract ADC value
                            adc_value = int(adc_value)
                            current_time = time.time() - start_time
                            data_points.append(adc_value)
                            times.append(current_time)
                            #print("ADC:", adc_value, "Time:", current_time, "seconds")
                            data_fileraw.write(f'{adc_value}, {current_time}\n') 
                if time.time() - start_time >= 61:  # Stop after 60 seconds
                    break
            


        window_size = 30 # Window size for moving average
        moving_averages = simple_moving_average(data_points, window_size) 
        with open(output_file_pathfiltered, 'w') as data_filefiltered: #'adc_data_filtered.data'
            for i in range(0,len(moving_averages)):
                data_filefiltered.write(f"{moving_averages[i]}, {times[i]}\n")

        with open(output_file_path, 'w') as data_file: 
            for i in range(0,len(moving_averages)):
                data_file.write(f"{moving_averages[i]}\n") #'adc_data.DATA'
                
        
        # Plotting the data
        plt.figure(figsize=(10, 5))
        plt.plot(times, data_points, label='Raw ADC Values')
        if len(moving_averages) > 0:
            time_indices_for_averages = times[window_size - 1:]  # Synchronize time indices
            plt.plot(time_indices_for_averages, moving_averages, label='Moving Average', linestyle='--')
        plt.xlabel('Time (s)')
        plt.ylabel('ADC Value')
        plt.title('ADC Value vs Time with Moving Average')
        plt.legend()
        plt.grid(True)
        # Save the figure to the output directory
        plt.savefig(output_graph_path)
        # Show the plot on screen
        plt.show()

    except serial.SerialException:
        print("Error: Unable to open serial port. Ensure the STM32 board is connected.")

if __name__ == "__main__":
    main()
