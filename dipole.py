import math

def dip(f, d):
    c = 299.792458
    lamb = c/f # Freq is in MHz
    denom = math.log((lamb/2)/d) - 0.429451
    num = 0.225706
    k = 1 - num/denom
    res = k * lamb / 2
    print("K Factor: " + str(k))
    print("L = " + str(res))

print("Gives the length of a \nhalf-wave dipole.")
print("USAGE: Call dip() w/")

print("1:Resonant freq (MHz)")
print("2:Element diameter (m)")

print("Example usage:")
print("dip(7.2,0.002)")
