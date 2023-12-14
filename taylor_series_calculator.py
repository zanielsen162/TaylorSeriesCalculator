from sympy import *
import sympy

x = Symbol('x')

# translate courtesy of Codeigo
superscript = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")

#finds the derivative values from the function, value, and degree 
def takeDeriv(f, n, c):
  count = 0
  func = f
  fc = (f.subs(x, c)).evalf()

  if (fc - int(fc)) == 0:
    fc = int(fc)
  else:
    fc = round(float(fc), 3)

  derivList = [fc]
  
  while count < n:
    func = diff(func, x)
    d = (func.subs(x, c)).evalf()

    if (d - int(d)) == 0:
      d = int(d)
    else: 
      d = float(d)
    
    derivList.append(d)
    count += 1

  return derivList

#provides denominator by calculating factorial
def factorials(n):
  count = 1
  factList = []
  value = 0

  while count <= n:
    value = factorial(count)
    factList.append(value)
    count += 1
  
  return factList

#formats values using above functions in Taylor Series equation
def format(fact, deriv, c, output):
  n = len(deriv)
  count = 1
  y1 = str(deriv[0])
  y2 = str(deriv[0])
  while count < n:
    term = str(round((deriv[count] / fact[count-1]), 3)) + "(x-" + str(c) + ")" + str(count).translate(superscript)
    term2 = str(deriv[count] / fact[count-1]) + "*(x-" + str(c) + ")**" + str(count)
    y1 = y1 + " + " + term
    y2 = y2 + " + " + term2
    count += 1

  if output:
    return y1
  else:
    return y2

#inputs and outputs
f = sympify(input("Function: "))
n = int(input("Order: "))
c = float(input("Center Value: "))
dlist = takeDeriv(f, n, c)
flist = factorials(n)
term = "(x-2)"

print("")
print("P(x) = " + str(format(flist, dlist, c, True)))
print("")

#finds the approximate value and compares to actual value
approxVal = float(input("Approximate: "))
listApprox = list(format(flist, dlist, c, False))
for i in listApprox:
  if i == 'x':
    listApprox[listApprox.index(i)] = str(approxVal)

eval = parse_expr("".join(listApprox), evaluate=False)

actual = f.subs(x, approxVal)
print("\nP(" + str(approxVal) + ") = " + str(round((eval.subs(x, approxVal)).evalf(), 3)))
print("Actual Value: " + str(actual))

error = ((actual - (eval.subs(x, approxVal)).evalf()) / actual) * 100
print("Percent Error: " + str(abs(error)))
