import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

# xoa dong nay di
import random

class GUI:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Computer Temperature Information Management System")
        # Create a frame to hold the labels and buttons
        frame = ttk.Frame(self.window)
        frame.pack()

        # Create labels for CPU, GPU, and HDD temperatures
        cpu_label = ttk.Label(frame, text="CPU Temperature:")
        gpu_label = ttk.Label(frame, text="GPU Temperature:")
        hdd_label = ttk.Label(frame, text="HDD Temperature:")
        cpu_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        gpu_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
        hdd_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)

        # Create labels to display the actual temperatures
        self.cpu_temp_string = tk.StringVar()
        self.gpu_temp_string = tk.StringVar()
        self.hdd_temp_string = tk.StringVar()
        cpu_temp_label = ttk.Label(frame, textvariable=self.cpu_temp_string)
        gpu_temp_label = ttk.Label(frame, textvariable=self.gpu_temp_string)
        hdd_temp_label = ttk.Label(frame, textvariable=self.hdd_temp_string)
        cpu_temp_label.grid(column=1, row=0, padx=5, pady=5, sticky=tk.E)
        gpu_temp_label.grid(column=1, row=1, padx=5, pady=5, sticky=tk.E)
        hdd_temp_label.grid(column=1, row=2, padx=5, pady=5, sticky=tk.E)

        # Initialize temperature values and history lists
        self.cpu_temp = random.randint(30, 90)
        self.gpu_temp = random.randint(30, 90)              # sua lai cho nay lay vao temp
        self.hdd_temp = random.randint(30, 90)
        self.cpu_temps = []
        self.gpu_temps = []
        self.hdd_temps = []

        # Create a figure and subplot to hold the temperature graph
        self.fig = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        # Add the graph to the GUI using a canvas widget
        canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Start a thread to update the temperature data and graph every second
        self.graph()

        # Create a button to export a report to a PDF file
        export_button = ttk.Button(frame, text="Export Report", command=self.export_report)
        export_button.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

        # Create a button to exit the program
        exit_button = ttk.Button(frame, text="Exit", command=self.exit)
        exit_button.grid(column=0, row=4, columnspan=2, padx=5, pady=5)

    # Method to update temperature data and graph
    def update_temperatures(self):
        # Get temperature values for CPU, GPU, and HDD
        self.cpu_temp = random.randint(30, 90)
        self.gpu_temp = random.randint(30, 90)              # sua lai cho nay lay vao temp
        self.hdd_temp = random.randint(30, 90)

        # Add new temperature data to lists
        self.cpu_temps.append(self.cpu_temp)
        self.gpu_temps.append(self.gpu_temp)
        self.hdd_temps.append(self.hdd_temp)
        
        # Delete the first element if the list have more than 40 elements
        if (len(self.cpu_temps) > 40):
            self.cpu_temps.pop(0)
        if (len(self.gpu_temps) > 40):
            self.gpu_temps.pop(0)
        if (len(self.hdd_temps) > 40):
            self.hdd_temps.pop(0)

        # Clear the graph and plot the new temperature data
        self.ax.clear()
        self.ax.plot(self.cpu_temps, label="CPU")
        self.ax.plot(self.gpu_temps, label="GPU")
        self.ax.plot(self.hdd_temps, label="HDD")

        # Add title and labels to the graph
        self.ax.set_title("Computer Temperature Graph")
        self.ax.get_xaxis().set_visible(False)
        self.ax.set_ylabel("Temperature (°C)")
        self.ax.legend()

        # Update the graph canvas with the new data
        self.fig.canvas.draw()

        # Update the temperature labels with new values
        self.cpu_temp_string.set(str(self.cpu_temp) + "°C")
        self.gpu_temp_string.set(str(self.gpu_temp) + "°C")
        self.hdd_temp_string.set(str(self.hdd_temp) + "°C")

        # Call this method again after 1000 milliseconds to update the graph again
        self.window.after(1000, self.update_temperatures)

    # Method to start a new thread for updating the temperature graph
    def graph(self):
        t = threading.Thread(target=self.update_temperatures)
        t.start()

    # Method to export a report of the current graph as an image
    def export_report(self):
        # Get the coordinates and dimensions of the window containing the graph
        x = self.window.winfo_rootx()
        y = self.window.winfo_rooty()
        w = self.window.winfo_width()
        h = self.window.winfo_height()

        # Define a bounding box that covers the entire window
        bbox = (x, y, x+w, y+h)

        # Take a screenshot of the window within the bounding box
        image = ImageGrab.grab(bbox)

        # Save the screenshot as a PNG file
        image.save("report.png")

    # Method to close the application window
    def exit(self):
        self.window.destroy()

    # Method to run the GUI application
    def run(self):
        # Start the main event loop for the application window
        self.window.mainloop()

# Create a new GUI object and run the application
if __name__=="__main__":
    gui = GUI()
    gui.run()
