import math

def dbm(watts):
    return 10 * math.log10((watts*1000))

def watt(dbm):
    return (math.pow(10, (dbm/10)))/1000

print("Calculates Watts from dBm\nand vice versa.")
print("USAGE:\nCall dbm() w/")

print("1:Wattage (W)")
print("Call watt() w/")
print("1:Decibels milliwatts (dBm)")

print("Example usage:")
print("watt(45.99)")