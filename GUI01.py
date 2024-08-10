import tkinter as tk
from tkinter import ttk

# Create a new tkinter window
root = tk.Tk()
root.title('Banana Interest Survey')
root.geometry('640x480+300+300')
root.resizable(False, False)

# Styling
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), background='white')
style.configure('TButton', font=('Arial', 12, 'bold'), background='brown', foreground='white')
style.configure('TCheckbutton', font=('Arial', 12))
style.configure('TRadiobutton', font=('Arial', 12))

# Main frame
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

# Title
title = ttk.Label(main_frame, text='Please take the survey', font=('Arial', 16, 'bold'))
title.grid(row=0, column=0, columnspan=2, pady=10)

# Name
name_label = ttk.Label(main_frame, text='What is your name?')
name_inp = ttk.Entry(main_frame)
name_label.grid(row=1, column=0, sticky=tk.W, pady=5)
name_inp.grid(row=1, column=1, sticky=(tk.W + tk.E), pady=5)

# Do you like to eat bananas?
eather_inp = ttk.Checkbutton(main_frame, text='Do you like to eat bananas?')
eather_inp.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)

# How many bananas per day?
num_label = ttk.Label(main_frame, text='How many bananas do you eat per day?')
num_inp = ttk.Spinbox(main_frame, from_=0, to=1000, increment=1)
num_label.grid(row=3, column=0, sticky=tk.W, pady=5)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E), pady=5)

# Best color for a banana
color_label = ttk.Label(main_frame, text='What is the best color for a banana?')
color_inp = tk.Listbox(main_frame, height=1)
color_label.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=5)
color_inp.grid(row=5, column=0, columnspan=2, sticky=(tk.W + tk.E), padx=25, pady=5)

# Add choices
color_choices = ('Any', 'Green', 'Green-Yellow', 'Yellow', 'Brown-Spotted', 'Black')
for choice in color_choices:
    color_inp.insert(tk.END, choice)

# Do you like plantains?
plantain_label = ttk.Label(main_frame, text='Do you like plantains?')
plantain_frame = ttk.Frame(main_frame)
plantain_yes_inp = ttk.Radiobutton(plantain_frame, text='Yes')
plantain_no_inp = ttk.Radiobutton(plantain_frame, text='Ewww, no!')
plantain_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_label.grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=5)
plantain_frame.grid(row=7, column=0, columnspan=2, sticky=tk.W, pady=5)

# Write a haiku
banana_haiku_label = ttk.Label(main_frame, text='Write a haiku about bananas')
banana_haiku_inp = tk.Text(main_frame, height=3, width=40, wrap='word')
banana_haiku_label.grid(row=8, column=0, columnspan=2, sticky=tk.W, pady=5)
banana_haiku_inp.grid(row=9, column=0, columnspan=2, sticky='NSEW', pady=5)

# Submit button
submit_btn = ttk.Button(main_frame, text='Submit Survey')
submit_btn.grid(row=10, column=0, columnspan=2, pady=10)

# Output line
output_line = ttk.Label(main_frame, text='', anchor='w', justify='left')
output_line.grid(row=11, column=0, columnspan=2, sticky='NSEW', pady=5)

# Add your GUI elements and logic here

# Start the tkinter event loop
root.mainloop()