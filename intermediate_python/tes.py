"""
Create functions that double, triple, quadruple the number received as a parameter.
"""

def multiplier(mult):
    def multi(number):
        return number * mult
    return multi


double = multiplier(2)
triple = multiplier(3)
quadruple = multiplier(4)

print(double(7))
print(triple(7))
print(quadruple(7))
