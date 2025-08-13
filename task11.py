# TASK---1

def factorial_with_loop(n):
  
  if n < 0:
    return "Factorial is not defined for negative numbers."
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result


sample_number = 5
calculated_factorial = factorial_with_loop(sample_number)

print(f"The factorial of {sample_number} is: {calculated_factorial}") 

