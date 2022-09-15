import sys
import numpy as np
# Include ~/PythonModule/ to the path
sys.path.append("../..")
import nuclear

# Input data
name = "Benzene"

Z = np.array([6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1])

xyz = np.array([
[ 0.0000000,  1.3916730, 0.0000000],
[ 1.2052240,  0.6958360, 0.0000000],
[ 1.2052240, -0.6958360, 0.0000000],
[ 0.0000000, -1.3916730, 0.0000000],
[-1.2052240, -0.6958360, 0.0000000],
[-1.2052240,  0.6958360, 0.0000000],
[ 0.0000000,  2.4695880, 0.0000000],
[ 2.1387260,  1.2347940, 0.0000000],
[ 2.1387260, -1.2347940, 0.0000000],
[ 0.0000000, -2.4695880, 0.0000000],
[-2.1387260, -1.2347940, 0.0000000],
[-2.1387260,  1.2347940, 0.0000000]
])

# Template for output file
out = """Molecule name:           {}

Total nuclear repulsion: {:^15.10f}
Total charge:            {:^15.10f}

Nuclear Dipole moment:
[       x                 y                 z       ]
[{:^15.10f}   {:^15.10f}   {:^15.10f}]
"""

# Write data out
with open("output.dat", "w") as outf:
    outf.write(out.format(
        name,
        nuclear.nuclear_repulsion(Z, xyz),
        nuclear.total_charge(Z),
        *nuclear.nuclear_dipole(Z, xyz)
        )
    )
