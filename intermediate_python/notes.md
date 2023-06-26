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

