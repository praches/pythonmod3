import math

def main():
  
  print("--- Mathematical Calculator ---")
  
  try:
   
    num_str = input("Please enter a number: ")
    number = float(num_str)

   
    if number <= 0:
      print("\nError: Please enter a positive number for square root and logarithm calculations.")
      
      sine_val = math.sin(number)
      print(f"The sine of {number} is: {sine_val:.4f}")
      return

   
    sqrt_val = math.sqrt(number)
    log_val = math.log(number) 
    sine_val = math.sin(number)

    
    print("\n--- Results ---")
    print(f"For the number: {number}")
    print(f"Square Root:    {sqrt_val:.4f}")
    print(f"Natural Log (e): {log_val:.4f}")
    print(f"Sine (radians): {sine_val:.4f}")

  except ValueError:
    #
    print("\nError: Invalid input. Please enter a valid number.")
  except Exception as e:
    
    print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
  main()
