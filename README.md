*Calculator*
This is a simple calculator app built with Python and Tkinter. It allows users to perform basic arithmetic operations.

Features
Performs addition, subtraction, multiplication, division and modulo operations
Clear button to delete entire input
Undo button to remove last digit entered
Displays error message for invalid inputs
Nice color schema using Tkinter styling

Usage
The calculator works like a normal handheld calculator:
Click the digit buttons to enter numbers
Click the operator buttons to perform a calculation
Click '=' to evaluate the expression and display the result
Click 'AC' to clear the input and display
Click '<-' to undo the previous digit entered

Code Overview
The code is structured as follows:
tkinter module is imported to create the GUI
ast module is used to evaluate math expressions safely
A Tk() root window is created
Tkinter widgets like Buttons and Entry are used to build the layout
Digit and operator buttons call functions to append them to the Entry
Equals button passes Entry input to ast.parse() to evaluate result
Try/except block catches errors and displays message
Functions defined for AC, undo, etc.
The styling is done using Tkinter properties like color, size, etc.

Installation
Requires Python 3 and tkinter module.
Clone the repository or download the calci.py file. Run python calci.py to launch the app.

Scope for Improvement
Some ways the calculator could be improved:
Add keyboard support for digit entry
Improve error handling for invalid expressions
Allow copying result to clipboard
Improve styling and layout
Add scientific calculator operations
Overall it covers the basics of building a simple GUI app with Tkinter.
