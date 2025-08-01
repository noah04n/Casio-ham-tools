import math
def qf(res_f, load, R, l=None, c=None):
    f = res_f * 1e6 # Convert MHz to Hz
    Q = 0
    if load == "y":
        if l:
            X = math.pi * 2 * f * l
        else:
            X = 1 / ( 2 * math.pi * f * c )
        Q = R / X

    else:
        if l:
            X = math.pi * 2 * f * l
        else:
            X = 1 / (math.pi * f * c )

        Q = X / R
        
    print("Quality factor:")
    print(Q)

print("Gives the RLC circuit's\nquality factor.")
print("Calculated w/ either\ncapacitance or\ninductance.")
print("USAGE: Call qf() w/")

print("1:Resonant freq (MHz)")
print("2:Circuit loaded (y/n)")
print("3:Resistance (Ohm)")
print("4:Inductance (Henry)")
print("5:Capacitance (Farad)")

print("Example usage:")
print("qf(14.128,'y',18000,l=2.7e-6)")