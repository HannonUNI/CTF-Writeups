import math
import hashlib
import sys
import numpy as np
SIZE = int(3e5)
VERIFY_KEY = "46e1b8845b40bc9d977b8932580ae44c"


def getSequence(A, B, n, m):

    n = len(A)
    m = len(B)

    # Pad sequences with zeros to the nearest power of 2
    padded_size = 2 ** int(np.ceil(np.log2(n + m - 1)))
    A_padded = np.pad(A, (0, padded_size - n), mode='constant')
    B_padded = np.pad(B, (0, padded_size - m), mode='constant')

    # Perform FFT on the padded sequences
    fft_A = np.fft.fft(A_padded)
    fft_B = np.fft.fft(B_padded)

    # Element-wise multiplication in frequency domain
    fft_result = fft_A * fft_B

    # Perform inverse FFT to get the convolution sequence
    result = np.fft.ifft(fft_result)

    # Take real part of the result (ignoring imaginary part)
    result = np.real(result)

    # Return the convolution sequence
    return result[:n + m - 1]


A = [0] * SIZE
B = [0] * SIZE

document1 = open("./rev3/Document 1.txt", "r")
nums1 = document1.readlines()

idx = 0

for num in nums1:
    A[idx] = int(num.strip())
    idx += 1

document2 = open("./rev3/Document 2.txt", "r")
nums2 = document2.readlines()

idx = 0

for num in nums2:
    B[idx] = int(num.strip())
    idx += 1


sequence = getSequence(A, B, SIZE, SIZE)
val = 0

for num in sequence:
    val = (val + num)

val = str(int(val))
print(val)
val_md5 = hashlib.md5(val.encode()).hexdigest()

if val_md5 != VERIFY_KEY:
    print("Wrong solution.")
    sys.exit(1)
else:
    print("Correct solution.")

key = str(hashlib.sha256(val.encode()).digest())
flag = "ctf{" + "".join(list([x for x in key if x.isalpha() or x.isnumeric()])) + "}"

print(flag)