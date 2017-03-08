'''
Created on May 9, 2016

@author: Gianni
'''

# Imports the GUI
from tkinter import *

def input(i):
    'Inputs the respective button that is being pressed in the calculator'
    global entry
    global result
    
    operators = ['%', '/', '*', '-', '+']
    
    # Clears the entry boxes if there was an error or a completed operation
    if (result.get().startswith(('Error: ', 'Result: '))):
        entry.delete(0, END)
        entry.insert(INSERT, '0')
        result.delete(0, END)
    
    # If input is clear
    if (i == 'AC'):
        entry.delete(0, END)
        entry.insert(INSERT, '0')
        result.delete(0, END)
        
    # If input is an operator
    elif any(i in s for s in operators):
        # If user attempts to input an operator when entry is empty nothing happens
        if (entry.get() == ''):
            entry.insert(INSERT,'')
        # If user attempts to input an operator when the only input is a decimal point or zero, nothing happens
        elif (entry.get() == '.') or (entry.get() == '0'):
            entry.insert(INSERT,'')
        # If user attempts to input multiple operators, only the last one will be considered
        elif (entry.get().endswith(' ')):
            cursor = len(entry.get())
            entry.delete(cursor - 3, END)
            entry.insert(INSERT, ' ' + i + ' ')
        # If user attempts to input an operator after a decimal point, only the last one will be considered
        elif (entry.get().endswith(' .')):
            cursor = len(entry.get())
            entry.delete(cursor - 4, END)
            entry.insert(INSERT, ' ' + i + ' ')
        else:
            entry.insert(INSERT, ' ' + i + ' ')
            
    # If input is compute
    elif (i == '='):
        # If entry divides by zero, returns an error
        if ((entry.get().endswith('/ 0')) or ('/ 0 ' in entry.get())):
            result.insert(INSERT, 'Error: Cannot Divide By Zero')
        # If entry is empty, nothing happens
        elif (entry.get() == ''):
            entry.insert(INSERT,'')
        # If user attempts to compute when the only input is a decimal point, nothing happens
        elif (entry.get() == '.'):
            entry.insert(INSERT,'')
        # If entry ends with an operation, it ignores it and computes up to last number
        elif (entry.get().endswith(' ')):
            cursor = len(entry.get())
            entry.delete(cursor - 3, END)
            res = eval(entry.get())
            result.insert(INSERT, 'Result: ' + str(res))
        # If entry ends with a decimal point, it ignores it and computes up to last number
        elif (entry.get().endswith(' .')):
            cursor = len(entry.get())
            entry.delete(cursor - 4, END)
            res = eval(entry.get())
            result.insert(INSERT, 'Result: ' + str(res))
        else:
            res = eval(entry.get())
            result.insert(INSERT, 'Result: ' + str(res))
            
    # If input is a number or a decimal point
    else:
        # If previous digit is a zero, ignores it if input is not a decimal point
        if ((entry.get().endswith(' 0') and i != '.') or (entry.get() == '0' and i != '.')):
            cursor = len(entry.get())
            entry.delete(cursor - 1, END)
            entry.insert(INSERT, i)
        # If user attempts to put multiple decimal points, puts an empty string instead
        elif((entry.get().endswith('.') and i == '.')):
            entry.insert(INSERT, '')
        else:
            entry.insert(INSERT, i)

# Constructor to instantiate a master
root = Tk()
root.wm_title('Calculator')

# Creates entries Frame and adds to top of root
entries = Frame(root)
entries.pack(side = TOP)

# Creates the entry Entry and adds to top of entries Frame
entry = Entry(entries, width = 41, relief = SUNKEN, borderwidth = 3)
entry.pack(side = TOP)
entry.insert(INSERT, '0')

# Creates the result Entry and adds to bottom of entries Frame
result = Entry(entries, width = 41, relief = SUNKEN, borderwidth = 3)
result.pack(side = BOTTOM)

# Creates the box Frame and adds to bottom of root
box = Frame(root)
box.pack(side = BOTTOM)

# For easier looping
rows = [['AC', '%', '/'],
          ['7', '8', '9', '*'],
          ['4', '5', '6', '-'],
          ['1', '2', '3', '+'],
          ['0', '.', '=']]

# Puts the each of the items in rows into a grid-layout through loops
for r in range(5):
    # For the AC and 0 rows
    if (r == 0 or r == 4):
        for c in range(3):
            # For the first column in the row
            if (c == 0):
                button = Button(box,
                            relief = RAISED,
                            padx = 10,
                            pady = 5,
                            width = 14,
                            text = rows[r][c],
                            command = (lambda i=(rows[r][c]): input(i))).grid(row = r, column = c, columnspan = 2)
            # For every other column
            else:
                button = Button(box,
                            relief = RAISED,
                            padx = 10,
                            pady = 5,
                            width = 5,
                            text = rows[r][c],
                            command = (lambda i=(rows[r][c]): input(i))).grid(row = r, column = c + 1)
    # For every other row
    else:
        for c in range(4):
            button = Button(box,
                            relief = RAISED,
                            padx = 10,
                            pady = 5,
                            width = 5,
                            text = rows[r][c],
                            command = (lambda i=(rows[r][c]): input(i))).grid(row = r, column = c)
            
# Runs the GUI
root.mainloop()