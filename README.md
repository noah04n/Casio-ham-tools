# Casio Calculator Ham Tools

This repo contains various useful calculation tools for amateur radio operators, specifically designed to run on Casio calculator models that support MicroPython.

When working on my ham radio projects I found myself performing certain calculations often. For example, I often made use of online calculators to calculate the dimensions of a Yagi-Uda antenna based on the operating frequency. I wanted to be able to do a large number of multi-step calculations right from my calculator so I wrote these various python files and designed them so that they can be run on the built-in MicroPython interpreter that is included on certain Casio calculators. 

Note: Most of the files have comments which you may want to remove after reading them since these calculators don't have very much storage. Each file also prints out instructions upon being run but aren't necessary to keep after the user has become familiarized with them.

73

## Resonance
The `resonance.py` script calculates the resonant frequency of an RLC/RL circuit in MHz given the inductance in Henrys and capacitance in Farads.

## Watts to dBm
The `watts_dbm.py` script provides two function to either convert Watts to dBm or dBm to Watts.

## Quality Factor
The `quality_factor.py` script provides a function to calculate the quality factor of a resonant circuit given its resistance in Ohms and one of either its capacitance in Farads or its inductance in Henrys.

## Dipole
The `dipole.py` script calculates the dimensions of a half-wave dipole antenna that, in general, exhibit more optimized resonance. Although the dimensions of a half-wave dipole are kind of in its name, better performance can be gained by considering how the diameter of the conducting elements affects its resonance. For this reason, these calculations will only give you more accurate results if your dipole has constant thickness, i.e. no telescoping antennas allowed!

The result is calculated using the following formula:
$$ L = K \frac{c}{f} $$
where $L$ is the length of the half-wave dipole, $c$ is the speed of light in m/s , $f$ is the frequency in Hz, and $K$ is a constant between 0 and 1. The constant $K$ can be calculated using the formula
$$K = 1 - \frac{0.225706}{ln\left(\frac{\lambda/2}{d}\right)-0.429451} $$
where lambda is the wavelength $\lambda = c/f$ and $d$ is the diameter of the dipole elements. This formula uses a model of a dipole in free space so, unless the dipole is being used for UHF or VHF where the wavelengths are small and the antenna is likely to be several wavelengths above ground, the calculation may not give the increased performance that we expect.
Reference: The ARRL Antenna Book: Vol 1, 25th Edition, Section 2.1 (Dipoles).
