import sys
import numpy as np
# Include ~/PythonModule/ to the path
sys.path.append("../..")
import nuclear

# Input data
name = "Water"

Z = np.array([8, 1, 1])

xyz = np.array([
[ 0.0000000,   0.0000000,   0.1653507],
[ 0.7493682,   0.0000000,  -0.4424329],
[-0.7493682,   0.0000000,  -0.4424329]
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
