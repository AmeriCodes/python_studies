### Functions

Introduction to functions (def) in Python
Functions are sections of code used to replicate a specific action throughout your code.
They can receive values for parameters (arguments) and return a specific value.
By default, Python functions return None (nothing).


Named and Unnamed Arguments in Python Functions.
A named argument has a name followed by an equal sign.
An unnamed argument only receives the argument (value).

```python
def soma(x, y, z):
    # Definition
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')
```
Default Values for Parameters
When defining a function, parameters can have default values. If a value is not provided for the parameter, the default value will be used.

Refactoring: Editing your code.

```python
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=}  {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
    
soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)
```

Scope of Functions in Python
Scope refers to the extent to which that code can reach.
There are global and local scopes.
The global scope is the scope where the entire code is accessible.
The local scope is the scope where only names within the same location can be accessed.



### Higher Order Functions - Functions that can receive and/or return other functions.

```python	
def apply_operation(func, lst):
    result = []
    for item in lst:
        result.append(func(item))
    return result

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
result = apply_operation(square, numbers)
print(result)  # Output: [1, 4, 9, 16, 25]
```

### First-Class Functions - Functions that are treated like other common data types (strings, integers, etc.).

```python
def create_power_function(exponent):
    def power_func(x):
        return x ** exponent
    return power_func

square = create_power_function(2)
cube = create_power_function(3)

print(square(2))  # Output: 4
print(cube(2))  # Output: 8
```

### Closure

In Python, a closure is a function that retains access to the variables of its enclosing scope even after the execution of that scope has finished. In other words, a closure is an inner function that "remembers" and has access to the variables of its outer function even when the outer function has completed execution.

A closure is created when an inner function references one or more variables from the outer function. These variables are "captured" by the inner function and remain alive within the closure, even if the outer function has already returned.

Closures are useful in situations where you need to create specialized functions that depend on a specific context, maintaining a consistent internal state. They are commonly used to create generator functions, decorators, and implement data encapsulation.

Here's a simple example of a closure in Python:

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)
print(result)  # Output: 15
```

In this example, the outer_function returns the inner function inner_function, which captures the variable x from the enclosing scope. When we call outer_function(10), it returns the closure inner_function with x set to 10. Then, we can call the closure as a regular function (closure(5)) and it adds x (10) to the passed argument (5), resulting in 15.

The ability of closures to capture and retain the state of outer variables is a powerful feature in Python, allowing for the creation of advanced and flexible functionalities.

