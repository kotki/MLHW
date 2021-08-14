import random as rnd
import math
import cmath

# # 1.
# def greetings():
#     userName = input()
#     print(f"Hello, {userName}!")

# # 2
# def summ3numbers():
#     numbers = [None] * 3
#     i = 0
#     while i < len(numbers):
#         number = input();
#         if(number.isnumeric()):
#             numbers[i] = int(number)
#             i+=1
#     print(f"Summ of 3 numbers is: {sum(numbers)}")


# # 3
# def prevNextNumbers():
#     number = 179;
#     nextNUmber = 179 + 1
#     prevNumber = 179 - 1
#     print(f"The next number for the number {number} is :{nextNUmber}")
#     print(f"The previous number for the number {number} is :{prevNumber}")

# # 4
# def findSquareSideByArea():
#     area = 25;
#     side = round(math.sqrt(area))
#     print(f"Side of a square with area {area} is {side}")

# # 5
# def triangleAreaAndPerimeter():
#     sides = [5,5,5]
#     expectedPerimeter = 15
#     expectedArea = 10.825317547305483
#     perimeter = getTrianglePerimeter(sides)
#     area = getTriangleArea(sides)
#     assert perimeter == expectedPerimeter, f"Perimeter should be equal to {expectedPerimeter}"
#     assert area == expectedArea, f"Area should be equal to {expectedArea}"
#     print(f"Perimeter of triangle {expectedPerimeter}")
#     print(f"Area of triangle {area}")


# def getTrianglePerimeter(sides):
#     return sides[0] + sides[1] + sides[2]

# def getTriangleArea(sides):
#     a = sides[0]
#     b = sides[1]
#     c = sides[2]
#     s = (a + b + c) / 2
#     return (s*(s-a)*(s-b)*(s-c)) ** 0.5

# # 6
# def credit():
#     creditAmount = 1000
#     creditPercent = 10
#     overpayment = int(creditAmount / 100 * creditPercent)
#     totalAmount = creditAmount + overpayment
#     shouldBeTotalAmount = 1100
#     shouldBeOverpayment = 100
#     assert shouldBeTotalAmount == totalAmount, f"Total amount should be equal to {totalAmount}"
#     assert shouldBeOverpayment == overpayment, f"Overpayment should be equal to {overpayment}"

# # 7
# def printArithmOperations(param1, param2):
#     if param1.isnumeric() and param2.isnumeric():
#         number1 = int(param1)
#         number2 = int(param2)
#         print(f" + : {number1 + number2}")
#         print(f" - : {number1 - number2}")
#         print(f" * : {number1 * number2}")
#         print(f" / : {number1 / number2}")
#     else:
#         print("Wrong input, one of parameters is not numeric")

# while 1:
#     printArithmOperations(input("First number: "),input("Second number: "))

# # 8
# def printRandomNumber(param1, param2):
#     if param1.isnumeric() and param2.isnumeric():
#         min = int(param1)
#         max = int(param2)
#         randomNumber = rnd.randint(min, max)
#         randomRationalNumber = rnd.uniform(min, max)
#         print(f"Random number generated between {min} and {max} is: {randomNumber}")
#         print(f"Random rational number generated between {min} and {max} is: {randomRationalNumber}")
#     else:
#         print("Wrong input, one of parameters is not numeric")

# while 1:
#     printRandomNumber(input("First number: "), input("Second number: "))

# # 9
# def prinMinNumber(param1, param2):
#     if param1.isnumeric() and param2.isnumeric():
#         number1 = int(param1)
#         number2 = int(param2)
#         if number1 < number2:
#             print(f"Less number if {number1}")
#         else:
#             print(f"Less number if {number2}")
#     else:
#         print("Wrong input, one of parameters is not numeric")

# while 1:
#     prinMinNumber(input("First number: "), input("Second number: "))

# # 10
# def printSign(param):
#     try:
#         number = int(param)
#         sign = 0
#         if number > 0:
#             sign = 1
#         elif number < 0:
#             sign = -1
#         print(f"Sign of a number is: {sign}")
#     except ValueError:
#         print("Wrong input, one of parameters is not numeric")

# while 1:
#     printSign(input("Number: "))

# # 11
# def printCalcOperation(param1, param2, operation):
#     allowedOperations = ["+", "-", "*", "/"]
#     if param1.isnumeric() and param2.isnumeric() and operation in allowedOperations:
#         number1 = int(param1)
#         number2 = int(param2)
#         result = None
#         if operation == "+":
#             result = number1 + number2
#         elif operation == "-":
#             result = number1 - number2
#         elif operation == "*":
#             result = number1 * number2
#         elif operation == "/" :
#             result = number1 / number2
#         print(f"Result of operation {operation} is : {int(result)}")
#     else:
#         print("Wrong input, one of parameters is not numeric or operation is not allowed")

# while 1:
#     printCalcOperation(input("First number: "), input("Second number: "), input("Operation: "))

# # 12 ax^2+bx+c=0
# def resolveQuadraticEquation(a, b, c):
#     d = (b**2) - (4*a*c)
#     _1 = (-b-cmath.sqrt(d))/(2*a)
#     _2 = (-b+cmath.sqrt(d))/(2*a)
#     return _1, _2

# sol1, sol2 = resolveQuadraticEquation(1,1,0)
# assert(sol1 == -1 and sol2 == 0)

# # 13
# def printTotalCostOfService(minutes, smsCount):
#     totalMinutes = int(minutes)
#     totalSMSCount = int(smsCount)
#     fixMinutes = 100
#     fixSmsCount = 30
#     costOfOneExtraMinute = 0.3
#     costOfOneExtraSms = 0.25
#     totalAmount = 30
#     if(fixMinutes < totalMinutes):
#         totalAmount += (totalMinutes - fixMinutes) * costOfOneExtraMinute
#     if(fixSmsCount < totalSMSCount):
#         totalAmount += (totalSMSCount - fixSmsCount) * costOfOneExtraSms
#     print(f"Total cons of service is: {totalAmount}")

# while 1:
#     printTotalCostOfService(input("Minutes: "), input("SMS: "))


# # 14
# def defineIfLetterIsWovelOrСonsonants(char):
#     vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
#     consonants = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "Q", "S", "T", "V", "X", "Z", "H", "R", "W", "b", "c", "d", "f", "g", "j", "k", "l", "m", "n", "p", "q", "s", "t", "v", "x", "z", "h", "r", "w"]
#     if char in vowels:
#         print("Char is Vowel")
#     elif char in consonants:
#         print ("Character is consonant")
#     else:
#         print("Char is neither vowel nor consonant")

# while 1:
#     defineIfLetterIsWovelOrСonsonants(input("Character: "))

# # 15
# def printTriangleForm(a,b,c):
#     if a == b == c:
# 	    print("Triangle is equilateral")
#     elif a==b or a==b or a==c:
# 	    print("Triangle is isosceles")
#     else:
# 	    print("Triangle is scalene")

# while 1:
#     printTriangleForm(input("Left: "), input("Botton: "), input("Right: "))