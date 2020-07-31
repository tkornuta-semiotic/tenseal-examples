# Based on the TenSEAL tutorial:
# https://github.com/OpenMined/TenSEAL/blob/master/tutorials/Tutorial%200%20-%20Getting%20Started.ipynb

import tenseal as ts
import numpy as np
from time import time

# Create context.
context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)



plain_vector1 = np.asarray([60, 66, 73, 81, 90])
plain_vector2 = np.asarray([1, 2, 3, 4, 5])

encrypted_vector1 = ts.bfv_vector(context, plain_vector1)
encrypted_vector2 = ts.bfv_vector(context, plain_vector2)

t_start = time()
_ = plain_vector1 * plain_vector2
t_end = time()
print("p2p multiply time: {} ms".format((t_end - t_start) * 1000))

t_start = time()
_ = encrypted_vector1 * plain_vector1
t_end = time()
print("c2p multiply time: {} ms".format((t_end - t_start) * 1000))

t_start = time()
_ = encrypted_vector1 * encrypted_vector2
t_end = time()
print("c2c multiply time: {} ms".format((t_end - t_start) * 1000))

