# Based on the TenSEAL tutorial:
# https://github.com/OpenMined/TenSEAL/blob/master/tutorials/Tutorial%200%20-%20Getting%20Started.ipynb

import tenseal as ts
import numpy as np

context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)

plain_vector = [60, 66, 73, 81, 90]
print("plain_vector: ", plain_vector)
encrypted_vector = ts.bfv_vector(context, plain_vector)
print("We just encrypted our plaintext vector of size:", encrypted_vector.size())
print("encrypted_vector.decrypt(): ", encrypted_vector.decrypt())

# Basic operations: encrypted +/-/* plain 
print("Ciphertext to plaintext (c2p) evaluations (add, sub and mul)")
add_result = encrypted_vector + [1, 2, 3, 4, 5]
print(add_result.decrypt())

sub_result = encrypted_vector - [1, 2, 3, 4, 5]
print(sub_result.decrypt())

mul_result = encrypted_vector * [1, 2, 3, 4, 5]
print(mul_result.decrypt())

print("Ciphertext to ciphertext (c2c) evaluations (add, sub and mul)")
encrypted_add = add_result + sub_result
print(encrypted_add.decrypt())


encrypted_sub = encrypted_add - encrypted_vector
print(encrypted_sub.decrypt())

encrypted_mul = encrypted_add * encrypted_sub
print(encrypted_mul.decrypt())
