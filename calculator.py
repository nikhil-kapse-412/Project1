# Calculator

from tkinter import *
from tkinter.messagebox import *
import re
from math import *

def open_multiplication():
    root.withdraw()
    multiplication_window.deiconify()

def back_to_main():
    multiplication_window.withdraw()
    root.deiconify()

def open_subtraction():
    root.withdraw()
    subtraction_window.deiconify()

def back_to_main_from_subtraction():
    subtraction_window.withdraw()
    root.deiconify()

def open_division():
    root.withdraw()
    division_window.deiconify()

def back_to_main_from_division():
    division_window.withdraw()
    root.deiconify()

def open_addition():
    root.withdraw()
    addition_window.deiconify()

def back_to_main_from_addition():
    addition_window.withdraw()
    root.deiconify()

def calculate_addition():
    try:
        num1 = addition_entry1.get()
        num2 = addition_entry2.get()
        if not num1:
            showerror("Issue", "Number 1 should not be empty")
            return
        if not num2:
            showerror("Issue", "Number 2 should not be empty")
            return
        elif num1.isalpha():
            showerror("Issue", "Number 1 should not be text")
            return
        elif num2.isalpha():
            showerror("Issue", "Number 2 should not be text")
            return
        num1 = float(num1)
        num2 = float(num2)
        result = num1 + num2
        addition_result_label.config(text=f"Result: {result:.2f}")

    except ValueError as e:
        showerror("Issue", "Do not enter special characters")

def calculate_subtraction():
    try:
        num1 = subtraction_entry1.get()
        num2 = subtraction_entry2.get()
        if not num1:
            showerror("Issue", "Number 1 should not be empty")
            return
        if not num2:
            showerror("Issue", "Number 2 should not be empty")
            return
        elif num1.isalpha():
            showerror("Issue", "Number 1 should not be text")
            return
        elif num2.isalpha():
            showerror("Issue", "Number 2 should not be text")
            return
        num1 = float(num1)
        num2 = float(num2)
        result = num1 - num2
        subtraction_result_label.config(text=f"Result: {result:.2f}")

    except ValueError as e:
        showerror("Issue", "Do not enter special characters")

def calculate_multiplication():
    try:
        num1 = multiplication_entry1.get()
        num2 = multiplication_entry2.get()
        if not num1:
            showerror("Issue", "Number 1 should not be empty")
            return
        if not num2:
            showerror("Issue", "Number 2 should not be empty")
            return
        elif num1.isalpha():
            showerror("Issue", "Number 1 should not be text")
            return
        elif num2.isalpha():
            showerror("Issue", "Number 2 should not be text")
            return
        num1 = float(num1)
        num2 = float(num2)
        result = num1 * num2
        multiplication_result_label.config(text=f"Result: {result:.2f}")

    except ValueError as e:
        showerror("Issue", "Do not enter special characters")

def calculate_division():
    try:
        no1 = division_entry1.get()
        no2 = division_entry2.get()
        if not no1:
            showerror("Issue", "Number 1 should not be empty")
            return
        if not no2:
            showerror("Issue", "Number 2 should not be empty")
            return
        elif no1.isalpha():
            showerror("Issue", "Number 1 should not be text")
            return
        elif no2.isalpha():
            showerror("Issue", "Number 2 should not be text")
            return
        no1 = float(no1)
        no2 = float(no2)
        if no2 == 0:
            showerror("Issue", "Number 2 cannot be zero")
            return
        result = no1/no2
        division_result_label.config(text=f"Result: {result:.2f}")

    except ValueError as e:
        showerror("Issue", "Do not enter special characters")

root = Tk()
root.title("Calculator")
root.geometry("600x600+50+50")
font = ("Arial", 30, "bold")

main_label = Label(root, text="Calculator", font=font)
main_label.pack(pady=5)

addition_button = Button(root, text="Addition", font=font, command=open_addition)
subtraction_button = Button(root, text="Subtraction", font=font, command=open_subtraction)
multiplication_button = Button(root, text="Multiplication", font=font, command=open_multiplication)
division_button = Button(root, text="Division", font=font, command=open_division)
addition_button.pack(pady=5)
subtraction_button.pack(pady=5)
multiplication_button.pack(pady=5)
division_button.pack(pady=5)

multiplication_window = Tk()
multiplication_window.title("Multiplication")
multiplication_window.geometry("600x600+40+40")

def clear_multiplication():
    multiplication_entry1.delete(0, END)
    multiplication_entry2.delete(0, END)
    multiplication_result_label.config(text="Result:")

multiplication_label1 = Label(multiplication_window, text="Enter Number 1: ", font=font)
multiplication_entry1 = Entry(multiplication_window, font=font)
multiplication_label2 = Label(multiplication_window, text="Enter Number 2: ", font=font)
multiplication_entry2 = Entry(multiplication_window, font=font)
multiplication_result_label = Label(multiplication_window, text="Result: ", font=font)
multiplication_calculate_button = Button(multiplication_window, text="Calculate", font=font, command=calculate_multiplication)
multiplication_clear_button = Button(multiplication_window, text="Clear", font=font, command=clear_multiplication)
multiplication_back_button = Button(multiplication_window, text="Back", font=font, command=back_to_main)
multiplication_label1.pack(pady=5)
multiplication_entry1.pack(pady=5)
multiplication_label2.pack(pady=5)
multiplication_entry2.pack(pady=5)
multiplication_result_label.pack(pady=5)
multiplication_calculate_button.pack(pady=5)
multiplication_clear_button.pack(pady=5)
multiplication_back_button.pack(pady=5)
multiplication_window.withdraw()

subtraction_window = Tk()
subtraction_window.title("Subtraction")
subtraction_window.geometry("600x600+40+40")

def clear_subtraction():
    subtraction_entry1.delete(0, END)
    subtraction_entry2.delete(0, END)
    subtraction_result_label.config(text="Result:")

subtraction_label1 = Label(subtraction_window, text="Enter Number 1: ", font=font)
subtraction_entry1 = Entry(subtraction_window, font=font)
subtraction_label2 = Label(subtraction_window, text="Enter Number 2: ", font=font)
subtraction_entry2 = Entry(subtraction_window, font=font)
subtraction_result_label = Label(subtraction_window, text="Result: ", font=font)
subtraction_calculate_button = Button(subtraction_window, text="Calculate", font=font, command=calculate_subtraction)
subtraction_clear_button = Button(subtraction_window, text="Clear", font=font, command=clear_subtraction)
subtraction_back_button = Button(subtraction_window, text="Back", font=font, command=back_to_main_from_subtraction)
subtraction_label1.pack(pady=5)
subtraction_entry1.pack(pady=5)
subtraction_label2.pack(pady=5)
subtraction_entry2.pack(pady=5)
subtraction_result_label.pack(pady=5)
subtraction_calculate_button.pack(pady=5)
subtraction_clear_button.pack(pady=5)
subtraction_back_button.pack(pady=5)
subtraction_window.withdraw()

division_window = Tk()
division_window.title("Division")
division_window.geometry("600x600+40+40")

def clear_division():
    division_entry1.delete(0, END)
    division_entry2.delete(0, END)
    division_result_label.config(text="Result:")

division_label1 = Label(division_window, text="Enter Number 1: ", font=font)
division_entry1 = Entry(division_window, font=font)
division_label2 = Label(division_window, text="Enter Number 2: ", font=font)
division_entry2 = Entry(division_window, font=font)
division_result_label = Label(division_window, text="Result: ", font=font)
division_calculate_button = Button(division_window, text="Calculate", font=font, command=calculate_division)
division_clear_button = Button(division_window, text="Clear", font=font, command=clear_division)
division_back_button = Button(division_window, text="Back", font=font, command=back_to_main_from_division)
division_label1.pack(pady=5)
division_entry1.pack(pady=5)
division_label2.pack(pady=5)
division_entry2.pack(pady=5)
division_result_label.pack(pady=5)
division_calculate_button.pack(pady=5)
division_clear_button.pack(pady=5)
division_back_button.pack(pady=5)
division_window.withdraw()

addition_window = Tk()
addition_window.title("Addition")
addition_window.geometry("600x600+40+40")

def clear_addition():
    addition_entry1.delete(0, END)
    addition_entry2.delete(0, END)
    addition_result_label.config(text="Result:")

addition_label1 = Label(addition_window, text="Enter Number 1: ", font=font)
addition_entry1 = Entry(addition_window, font=font)
addition_label2 = Label(addition_window, text="Enter Number 2: ", font=font)
addition_entry2 = Entry(addition_window, font=font)
addition_result_label = Label(addition_window, text="Result: ", font=font)
addition_calculate_button = Button(addition_window, text="Calculate", font=font, command=calculate_addition)
addition_clear_button = Button(addition_window, text="Clear", font=font, command=clear_addition)
addition_back_button = Button(addition_window, text="Back", font=font, command=back_to_main_from_addition)
addition_label1.pack(pady=5)
addition_entry1.pack(pady=5)
addition_label2.pack(pady=5)
addition_entry2.pack(pady=5)
addition_result_label.pack(pady=5)
addition_calculate_button.pack(pady=5)
addition_clear_button.pack(pady=5)
addition_back_button.pack(pady=5)
addition_window.withdraw()

def close_program():
    if askokcancel("Quit", "Do you want to exit?"):
        multiplication_window.destroy()
        subtraction_window.destroy()
        division_window.destroy()
        addition_window.destroy()

multiplication_window.protocol("WM_DELETE_WINDOW", close_program)
subtraction_window.protocol("WM_DELETE_WINDOW", close_program)
division_window.protocol("WM_DELETE_WINDOW", close_program)
addition_window.protocol("WM_DELETE_WINDOW", close_program)

root.mainloop()
