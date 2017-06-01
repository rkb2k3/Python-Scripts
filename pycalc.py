#!/usr/bin/python

arithmetic_operator = raw_input("Enter the arithmetic operator: ")
operand1 = int(input("Enter the first operand: "))
operand2 = int(input("Enter the second operand: "))

if arithmetic_operator == "+":
	print(operand1 + operand2)

elif arithmetic_operator == "-":
	print(operand1 - operand2)

elif arithmetic_operator == "*":
	print(operand1 * operand2)

elif arithmetic_operator == "/":
        print(operand1 / operand2)



