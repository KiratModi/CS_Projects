"""
Not able to write as many as I wanted due to time but structure is written by me and shapes are taken from my previous projects which I had build earlier I could have added
more shapes but I dont remember the tricks at a moment
"""


import turtle
import tkinter as tk
from tkinter import simpledialog

# Initialize the turtle screen and turtle object
screen = turtle.Screen()
t = turtle.Turtle()

# Function to move the turtle
def move_turtle(direction, distance):
    if direction == 'up':
        t.setheading(90)
    elif direction == 'down':
        t.setheading(270)
    elif direction == 'left':
        t.setheading(180)
    elif direction == 'right':
        t.setheading(0)
    t.forward(distance)

# Function to rotate the turtle
def rotate_turtle(angle):
    t.right(angle)

# Function to draw shapes
def draw_shape(shape):
    if shape == 'circle':
        t.circle(50)
    elif shape == 'square':
        for _ in range(4):
            t.forward(100)
            t.right(90)
    elif shape == 'triangle':
        for _ in range(3):
            t.forward(100)
            t.right(120)
    elif shape == 'star':
        for _ in range(5):
            t.forward(100)
            t.right(144)
    elif shape == 'hexagon':
        for _ in range(6):
            t.forward(100)
            t.right(60)
    elif shape == 'custom':
        # Just added random coordinates 
        for _ in range(8):
            t.forward(50)
            t.right(45)

# UI and input
def process_input(command):
    if command.lower() == 'quit':
        screen.bye()  # Close the turtle screen
        root.destroy()  # Close the Tkinter window
        return True  # Indicate that the program should quit
    elif command.lower() == 'move':
        direction = simpledialog.askstring("Input", "Enter direction (up, down, left, right, rotate):")
        if direction in ['up', 'down', 'left', 'right']:
            distance = simpledialog.askinteger("Input", f"Enter distance to move {direction}:")
            move_turtle(direction, distance)
        elif direction == 'rotate':
            angle = simpledialog.askinteger("Input", "Enter angle to rotate:")
            rotate_turtle(angle)
    elif command.lower() == 'draw':
        shape = simpledialog.askstring("Input", "Enter shape (circle, square, triangle, star, hexagon, custom):")
        draw_shape(shape)
    return False  # Indicate that the program should continue

# Setting up Tkinter for input dialogs
root = tk.Tk()
root.withdraw()  # Hide the root window

# Main loop to get commands from the user
while True:
    command = simpledialog.askstring("Input", "Enter command (move, draw, or quit):")
    if command:
        if process_input(command):
            break  # Exit the loop if the user enters 'quit'
    else:
        break

# Close the Tkinter window if not already closed
if root.winfo_exists():
    root.destroy()

# Close the turtle screen if not already closed
if screen._root is not None:
    screen.bye()
