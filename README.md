1. Factorial Calculator->
   
This script provides a function to calculate the factorial of a non-negative integer using a for loop.

Functionality ⚙️

->The factorial_with_loop(n) function takes an integer n as input and computes its factorial (n).

->Iterative Calculation: It uses a for loop to multiply all integers from 1 up to the given number n.

Base Case Handling:

->Correctly returns 1 for the input 0 (since 0=1).

->Returns an informative string "Factorial is not defined for negative numbers." for any negative input.

2. Mathematical Calculator->

This is a command-line tool that prompts a user for a number and performs several mathematical operations using Python's math module.

Features ✨
The script calculates the following for a user-provided number:

Square Root: 
sqrtx

Natural Logarithm: 
ln(x)

Sine: 
sin(x) (input angle is assumed to be in radians)

How It Works->

->User Input: The program prompts the user to enter a number in the console.

->Error Handling: It's wrapped in a try-except block to gracefully handle errors:

->ValueError: Catches non-numeric input (e.g., "abc").

->Exception: Catches any other unexpected runtime errors.

Input Validation: The script checks if the number is positive. For square root and logarithm calculations, a positive number is required. If the input is zero or negative, it prints an error message but still proceeds to calculate the sine value.

Formatted Output: All results are neatly printed and formatted to four decimal places for better readability.
