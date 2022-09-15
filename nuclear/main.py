import numpy as np

def nuclear_repulsion(at_nums, coords):
    """ Compute the nuclear repulsion energy (in Hartrees) of a
    collection of atoms.

    Arguments:

    at_nums -- numpy array of atomic numbers.
    coords  -- corresponding numpy array with atomic coordinates (in Bohr).
    """
    # Ensure the length of `at_nums` equals `coords`
    assert len(at_nums) == len(coords)
    N = len(at_nums)

    # Initialize the output number
    out = 0.0

    # Loop through unique pair of atoms
    # i.e. i runs from 0 to (N-1) and j from (i+1) to (N-1)
    for i in range(N):
        for j in range(i+1, N):

            # Computes distance between atom i and j
            dist = np.sqrt(np.sum((coords[i] - coords[j])**2))

            # Add i,j contribution to the output
            out += at_nums[i] * at_nums[j] / dist

    return out

def nuclear_dipole(at_nums, coords):
    """ Compute the nuclear dipole vector of a 
    collection of atoms.

    Arguments:

    at_nums -- numpy array of atomic numbers.
    coords  -- corresponding numpy array with atomic coordinates (in Bohr).
    """
    # Note that the first index of `coords` correspond to a specific Z
    return np.einsum("Z,Zi->i", at_nums, coords) 

def total_charge(at_nums):
    """ Compute the total charge of a collection of nuclei.

    Arguments:

    at_nums -- numpy array of atomic numbers.
    """
    return sum(at_nums)
