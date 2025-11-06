#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(side, otherside, thirdside):
    perimeter = side + otherside + thirdside
    return perimeter/2



def multiplyDifferences(sPerimeter, side, otherside, thirdside):
    sideDif = sPerimeter - side
    othersideDif = sPerimeter - otherside
    thirdsideDif = sPerimeter - thirdside
    return sPerimeter*sideDif*othersideDif*thirdsideDif

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.

def herons(side, otherside, thirdside):
    sPerimeter = semiPerimeter(side, otherside, thirdside)
    mDiffernces = multiplyDifferences(sPerimeter, side, otherside, thirdside)
    return root(mDiffernces)


#quadratic equation
def quadratic_eq(a, b, c):
    discrimanant = root((b**2)-(4*a*c))
    return ((-b) - discrimanant) / 2*a

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(number):
    return 2*number

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(one, two):
    one = -one
    return (one - two),(one + two)
#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a, b, c):
    return ((b**2) - (a*c*4))

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a, b, c):
    Discriminant = root(mainCalc(a, b, c))
    both_answers = (plusMinus(b, Discriminant))
    return (both_answers[0]/denominator(a)), (both_answers[1]/denominator(a))