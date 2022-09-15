import numpy as np
import sys
sys.path.append("/home/gustavo/PythonModuleExample")
import nuclear

# Use a square arrangement of H and He for testing
#   H ...... He
#   .        .
#   .        .
#   .        .
#   H....... H

Z = np.array([1, 2, 1, 1])

xyz = np.array([
[-0.5,  0.5, 0.0],
[ 0.5,  0.5, 0.0],
[-0.5, -0.5, 0.0],
[ 0.5, -0.5, 0.0]
])

def test_nuclear_repulsion():
    assert nuclear.nuclear_repulsion(Z, xyz) == 6.0 + 3/np.sqrt(2)

def test_total_charge():
    assert nuclear.total_charge(Z) == 5.0

def test_nuclear_dipole():
    assert np.allclose(nuclear.nuclear_dipole(Z, xyz), [0.5, 0.5, 0.0])
