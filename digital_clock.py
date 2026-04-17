import tkinter as tk
from time import strftime

def time():
    # Format the current time
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    # Call the time function again after 1000ms (1 second)
    label.after(1000, time)

# Initialize the main window
root = tk.Tk()
root.title("Digital Clock")

# Style the label for the clock
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

# Start the clock
time()

# Run the application
root.mainloop()
