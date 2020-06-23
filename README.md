# BananacClt
A calculator clt that performs like a banana developed in python

# Usage

## Execution
- You'll need to install Python, at least the latest version: https://www.python.org/
- Go to folder of the project, and type in terminal:
`python3 Banana.py`
or
`python Banana.py`

## Help Information and Quit
`-q #will quit the program`
`-h #will display an help information about BananacClt`

## Operators
For now you can use these operations:
`-+ #sum`
`-- #subtraction`
`-/ #division`
`-* #multiplication`
`-** #potetiation`
`-// #root`

## Format Expression
The usage is simple, you basically need to type the command in this format:
`Value1 Value2 ... ValueN -Operation`
Example of a sum:
`2 2 -+`

## Summation and Product
It's easy to do a Summation or a Product:
### Summation
`3 4 5 2 20 45 60 15 75 -+`
result: `229.0`
### Product
`3 4 5 2 20 45 60 15 75 -*`
result: `7290000000.0`

## Creating Functions
You can create your own functions too, you'll need to define in this format:
`def f(arguments): (Value1 or Variable1) .... (ValueN or VariableN) -Operation`
### Example:
the following function will calculate an percentage: 
`def f(x):x 1.5 -*`
You can call your function:
`f(4)`
result:`6.0`

# Goals
- Add conditional function support
- Add more useful operations(derivative,integral,etc)
- Add support to base numbers