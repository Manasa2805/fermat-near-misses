'''
Title: Near Misses Finder for Fermat's Last Theorem
File name: near_Misses.py
External files required: N/A
External files created: N/A
Teammate 1:Pravallika Nagalakunta
Email: pravallikanagalaku@lewisu.edu
Teammate 2:Manasa Keerthi
Email:manasaKeerthi@lewis.edu 
Course Number: Software Engineering- In person, FA24-CPSC-60500-001
Date completed: September 22, 2024
Program Description: This program calculates the nearest misses for integer solutions to x^n + y^n = z^n
where x, y, and z are integers, and n is the power. It identifies the smallest relative miss from the perfect integer solutions.
'''
import math
import tkinter as tk
from tkinter import simpledialog

def calculate_near_misses(n, k, output):
    """Calculate the closest misses to x^n + y^n = z^n for given n and k, and update the output label."""
    smallest_miss = None
    best_combination = None
    # Iterate over all possible values of x and y within the range [10, k]
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            sum_powers = x ** n + y ** n
            z = math.floor(sum_powers ** (1 / n))
            # Calculate z^n and (z+1)^n to determine the nearest integer solutions
            z_power = z ** n
            z1_power = (z + 1) ** n

            # Calculate absolute misses from z^n and (z+1)^n
            miss1 = sum_powers - z_power
            miss2 = z1_power - sum_powers
            miss = min(miss1, miss2)
            relative_miss = miss / sum_powers

            # Update the smallest miss found
            if smallest_miss is None or relative_miss < smallest_miss:
                smallest_miss = relative_miss
                best_combination = (x, y, z, miss, relative_miss)
    
    # Display the results in the GUI
    if best_combination:
        result = (f"x={best_combination[0]}, y={best_combination[1]}, z={best_combination[2]}, "
                  f"miss={best_combination[3]}, relative miss={best_combination[4]:.8f}")
        output.config(text=result)

def main():
    """Initialize the GUI and handle user inputs for n and k."""
    root = tk.Tk()
    root.title("Find Near Misses")

    label = tk.Label(root, text="Enter n and k values:")
    label.pack(pady=10)

    n_entry = simpledialog.askinteger("Input", "Enter the power n (3 <= n <= 11):", parent=root)
    k_entry = simpledialog.askinteger("Input", "Enter the upper limit k (k >= 10):", parent=root)

    output = tk.Label(root, text="", wraplength=400)
    output.pack(pady=20)

    # Process user inputs if valid
    if n_entry and k_entry:
        calculate_near_misses(n_entry, k_entry, output)

    root.mainloop()

if __name__ == "__main__":
    main()

