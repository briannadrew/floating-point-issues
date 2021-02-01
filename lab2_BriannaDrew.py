# lab2_BriannaDrew.py

# Brianna Drew
# January 31, 2021
# ID: #0622446
# Lab #2

# Part #1: I noticed that .1 + .1 = .2 was determined to be true, but both .1 + .1 + .1 = 3 as well as .1 + .1 + .1 + .1 = 4 were determined
#          to be false, even though they both should be true.
#
# Part #2: For 10 iterations, 6 of them were correct (60%). For 100 iterations, 11 of them were correct (11%). For 1,000 iterations, 16
#          of them were correct (1.6%). While the number of correct results increases as the number of iteratons increases, the percentage
#          drastically decreased the more iterations were added. The difference between the correct and incorrect sums between the different
#          amount of iterations increase by 2 decimal places (a.k.a. the number of 0s directly after the radix point in the difference
#          decreases by 2) each time you multiply the iterations by 10. So, there's 15 0s after the radix point for 10 iterations, 13 for
#          100 iterations, and 11 for 1,000 iterations. So, to get to just 1 0 after the radix point, we would have to multiply by 10 5
#          more times, and then by 5 to take the last 0 off. Therefore, I estimate that it would take approximately 500,000,000 iterations
#          to get an error of 0.1 (the number we're adding).
#
# Part #3: Adding 0.2 together for 100 iterations produces a difference of 3.907985046680551e-14 with 11 correct calculations. 0.7 also
#          produces an incorrect result, with 10 correct calculations and a difference of 1.2789769243681803e-13. Two numbers that produce
#          the correct sum with a difference of 0 and 100 correct calculations is 0.5 and 1.5. When doing some research as to why these
#          specific floats when added together produced the correct result whereas others didn't seems to do with scientific notations and
#          how these numbers are stored as binary. When floating point numbers are stored in binary, there are 3 components: sign, exponent,
#          and mantissa. The sign is whether the number is negative or positive, the exponent is basically where the radix point is (the
#          exponent in scientific notation), and the mantissa is the actual number. When it comes to scientific notation, the floats in
#          python are actually represented as an integer multiplied by an integer power of 2. Therefore, many of them simply do not fit into
#          this criteria, so then they are stored as the closest approximation that does fit that criteria. The reason that floats that
#          have a 5 and a 5 only after the radix point is that, simply put, it can be respresented exactly how it is as an integer multiplied
#          by an integer power of 2. To further explain this, 0.5 can also be represented as 1/2, and 1.5 can also be represented as 3/2.
#          Therefore, that denominator of 2 will fit perfectly into the criteria of being an integer multiplied by an integer power of 2 in
#          scientific notation. When represented in binary, this will result in the mantissa being much less complicated (less 1s and more 0s)
#          than floats like 0.2 or 0.7 which do not perfectly fit that criteria without approximation, making it easier to store accurately.
#          (Source: https://stackoverflow.com/questions/21895756/why-are-floating-point-numbers-inaccurate)
#
# Part #4: Using the decimal datatype, it appears to result in no errors, with calculations at each iteration being 100% accurate and results
#          in an error difference of 0 with 10, 100, and 1,000 iterations. Therefore, it is much better than using Python's default float
#          datatype in terms of accuracy and arithmetic. The only thing I will say is that there are some limiations, one that I ran into
#          being that division may not be accurate as the result will automatically be a float. The reason this datatype provides better
#          accuracy when working with floating point numbers is that all floats are stored as an IEEE double-precision format. The decimal
#          datatype, however, allows for a much higher precision and lower range than floats, which will result in much more accurate results.
#          More specifically, the float's default precision is 18 places and the decimal's default precision is 28 places. Another advantage
#          to the decimal datatype over the float datatype is that the decimal module is that it allows the user to be able to adjust the
#          precision if desired, but I did not need to for this lab.
#          (Sources: https://docs.python.org/3/library/decimal.html and https://zetcode.com/python/decimal/)

# import required modules
from decimal import *

floatSum = 0
decSum = 0
toAddFloat = .1 # number to continually add together as a float
toAddDec = Decimal(".1") # number to continually add together as a decimal
max = 100 # number of iterations
floatCorrect = 0
decCorrect = 0

# continually add toAddFloat as floats together for specified number of iterations
for i in range (0, max, 1):
    floatSum = floatSum + toAddFloat
    if (floatSum == round((i + 1) * toAddFloat, 1)): # check if the addition is what it should be
        floatCorrect += 1

# continually add toAddDec (.1) as decimals together for specified number of iterations
for i in range (0, max, 1):
    decSum = decSum + toAddDec
    if (decSum * 10 == (i + 1)): # check if the addition is what it should be
        decCorrect += 1

# print out the results
print("\nFLOAT RESULTS:")
print("--------------")
print("Iterations: ", max, ", Added Number: ", toAddFloat, ", Calculated Sum: ", floatSum, ", Correct Result: ", toAddFloat * max,
        ", Difference: ", abs((toAddFloat * max) - floatSum), ", Times Correct: ", floatCorrect, "\n")

print("DECIMAL RESULTS:")
print("----------------")
print("Iterations: ", max, ", Added Number: ", toAddDec, ", Calculated Sum: ", decSum, 
        ", Correct Result: ", toAddDec * max, ", Difference: ", abs((toAddDec * max) - decSum), ", Times Correct: ", decCorrect)