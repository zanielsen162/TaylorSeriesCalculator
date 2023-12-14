# Taylor Series Approximation Calculator

This Python program calculates the Taylor series approximation for a given function up to a specified order and center value. It uses the SymPy library to handle symbolic expressions and perform differentiation.

## Prerequisites

Ensure you have Python installed on your system and install the SymPy library using the following command:

```bash
pip install sympy
```

## Usage

1. Open the terminal or command prompt.

2. Run the program by executing the following command:

    ```bash
    python taylor_series_calculator.py
    ```

3. Enter the function, order, and center value as prompted.

4. The program will output the Taylor series approximation for the given function up to the specified order.

5. You will be prompted to input an approximate value for which the program will calculate the approximate function value and compare it to the actual value.

## Functions

### `takeDeriv(f, n, c)`

This function calculates the derivative values of the given function at the specified center up to the specified order.

### `factorials(n)`

This function calculates the factorials up to the specified order.

### `format(fact, deriv, c, output)`

This function formats the Taylor series equation using the calculated factorials and derivatives.

## Example

Here is an example of the program output:

```bash
Function: exp(x)
Order: 4
Center Value: 0

P(x) = 1 + x + x**2/2 + x**3/6 + x**4/24

Approximate: 1.5

P(1.5) = 4.481
Actual Value: 4.48169
Percent Error: 0.001
```

In this example, the Taylor series approximation for the function `exp(x)` up to the 4th order and center value 0 is calculated. The program then compares the approximate value with the actual value, providing the percent error.

Feel free to experiment with different functions, orders, and center values to explore various Taylor series approximations!
