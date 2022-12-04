import math

print("Please select from the list below.")
print("1 - Addition, 2 - Subtraction, 3 - Multiplication, 4 - Division, 5 - Square Root, 6 - Square, 7 - Pythagoreas Theorem.")
input_1 = int(input("Please enter the number next to the operation you want to perform:"))




if input_1 == 1:

        input_1 = int(input("What is your first number?"))
        input_2 = int(input("What is your second number?"))

        sum_input = input_1 + input_2

        print("The sum of the two numbers given is", sum_input)
        
if input_1 == 2:

        input_11 = int(input("What is your first number?"))
        input_22 = int(input("What is your second number?"))

        summ_input = input_11 - input_22

        print("The difference of the two numbers given is", summ_input)


if input_1 == 3:

        input_111 = int(input("What is your first number?"))
        input_222 = int(input("What is your second number?"))

        prod_input = input_111 * input_222

        print("The product of the two numbers given is", prod_input)


if input_1 == 4:

        input_1111 = int(input("What is your first number?"))
        input_2222 = int(input("What is your second number?"))

        input_q = input_1111 / input_2222

        print("The quotient of the two numbers given is", input_q)


if input_1 == 5:

        input_1s = int(input("What number do you want to square?"))
        input_1ss = input_1s * input_1s

        print(input_1s, "squared is", input_1ss)


if input_1 == 6:

        input_1sr = int(input("What number do you want to find the square root of?"))
        input_1rs = math.sqrt(input_1sr)

        print("The square root of", input_1sr, "is", input_1rs)



if input_1 == 7:

        input_1pt = int(input("What is the value of the first leg?"))
        input_2pt = int(input("What is the value of the second leg?"))

        pt = input_1pt * input_1pt
        pt2 = input_2pt * input_2pt

        pt3 = pt + pt2

        final_answer = math.sqrt(pt3)

        print("The value of the hypotneuse is", final_answer)
