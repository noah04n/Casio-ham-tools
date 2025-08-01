import math

def r(l=0, c=0):
    res = 1/math.sqrt((l*c))
    res_MHz = res/(2*math.pi)/1000000
    print("Resonant frequency:")
    print(str(res_MHz) + " MHz")

print("Gives the RLC/LC circuit's\nresonant frequency.")
print("USAGE: Call r() w/")

print("1:Inductance (Henry)")
print("2:Capacitance (Farad)")
print("Parallel & series\ngive the same result.")

print("Example usage:")
print("r(2.7e-6,2e-12)")
