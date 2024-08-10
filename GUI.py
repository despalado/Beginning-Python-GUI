import tkinter as tk

# Create a new tkinter window
root = tk.Tk()
root.title('Banana interest survey')
root.geometry('640x480+300+300')
root.resizable(False, False)

title = tk.Label(root,text='Please take the survery',font =('Arial, 16 bold'),bg='brown',fg='#FF0')
title.grid()
# title.grid(row=1,column=1)
name_label = tk.Label(root,text='What is your name?')
name_inp = tk.Entry(root)
name_label.grid(row=1,column=0)
name_inp.grid(row=1,column=1)

eather_inp = tk.Checkbutton(root,text='Do you like to eat bananas?')
eather_inp.grid(row=2,columnspan=1,sticky='we')

num_label = tk.Label(root,text='How many bananas do you eat per day?')
num_inp = tk.Spinbox(root, from_=0, to=1000, increment=1)
num_label.grid(row=3,sticky=tk.W)
num_inp.grid(row=3,column=1,sticky=(tk.W + tk.E))

color_label = tk.Label(root,text='What is the best color for a banana?')
color_inp = tk.Listbox(root, height = 1) # only show selected item.
color_label.grid(row=4,columnspan=2,sticky=tk.W, pady=10)
color_inp.grid(row=5,columnspan=2,sticky=tk.W + tk.E, padx=25)

# # add choices
color_choices = ('Any', 'Green', 'Green-Yellow', 'yellow','Brown- Spotted', 'Black')

for choice in color_choices:
    color_inp.insert(tk.END, choice)

plantain_label = tk.Label(root,text='Do you like plantains?')
plantain_frame = tk.Frame(root)
plantain_yes_inp = tk.Radiobutton(plantain_frame, text='Yes')
plantain_no_inp = tk.Radiobutton(plantain_frame, text='Ewww, no!')

plantain_yes_inp.pack(side ='left',fill='x',ipadx = 10, ipady=5)
plantain_no_inp.pack(side ='left',fill='x',ipadx = 10, ipady=5)
plantain_label.grid(row=6,columnspan=2,sticky=tk.W)
plantain_frame.grid(row=7,columnspan=2,sticky=tk.W)

banana_haiku_label = tk.Label(root,text='Write a haiku about bananas')
banana_haiku_inp = tk.Text(root, height=3)
banana_haiku_label.grid(row=8,sticky=tk.W)
banana_haiku_inp.grid(row=9,columnspan=2,sticky='NSEW')

submit_btn = tk.Button(root, text='Submit Survey')
submit_btn.grid(row=99)

output_line = tk.Label(root, text='',anchor='w',justify='left')
output_line.grid(row=100,columnspan=2,sticky='NSEW')

# Add your GUI elements and logic here

# Start the tkinter event loop
root.mainloop()