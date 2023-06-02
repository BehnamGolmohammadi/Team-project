from addition import *
from amin import *
from anahita import *
from Behnam import *
from niko import *
from nima import *

while True:
    try:
        num1, oper, num2 = input("Enter your formula:\n>>> ").split()
        num1, num2 = float(num1), float(num2)
        match oper:
            case "+":
                print(f"result = {function(num1, num2)}")
            case "-":
                print(f"result = {sub_func(num1, num2)}")
            case "*":
                print(f"result = {multipluy(num1, num2)}")
            case "/":
                print(f"result = {div_func(num1, num2)}")
            case "%":
                print(f"result = {mod_func(num1, num2)}")
            case "**":
                print(f"result = {power_func(num1, num2)}")

    except Exception as err:
        print(f"Error: {err}")
        print("Quit")
        quit()
