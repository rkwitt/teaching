# Ex. 2 template

# Some imports
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

def compute_row_norms(A):
    if sp.issparse(A):
        return spla.norm(A, axis=1)
    return np.linalg.norm(A, axis=1)


def normalize_matrix(A, row_norms):
    normalization_matrix = sp.diags(1 / row_norms)
    return normalization_matrix @ A


def normalize_system(A, b):
    if not sp.issparse(A):
        A = np.array(A)

    row_norms = compute_row_norms(A)
    A = normalize_matrix(A, row_norms=row_norms)
    b = np.array(b).ravel() / row_norms

    return A, b, row_norms

def kaczmarz(A,b):
    # YOUR CODE GOES HERE
    # return x_k
    pass

# UNCOMMENT AND COMPLETE
# A = np.array(...).astype('float32')
# b = np.array(...).astype('float32')
#
# sol = kaczmarz(A,b)


