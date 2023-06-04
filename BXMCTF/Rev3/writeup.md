# MCV5U (not ez)

Author: Ryzon

Ryzon, who just finished his ICS5U class, forgets that he also needs to finish his final MCV5U assignment, which is due on the same day!

Unfortunately, all of Ryzon's brain cells are destroyed due to how scuffed ICS5U is, and he begs you, his friend, to help him finish this assignment for him.

---

SPECIAL NOTE, PLEASE READ

The flag format for this problem is different from the rest, it is: `ctf{[!-z]{6,128}}` (the part inside the bracket can be any string of 6-128 printable ASCII characters, including letters, numbers, and symbols).

---

#### files

[Document 1.txt
](./Document 1.txt)

[Document 1.txt](Document 1.txt)

[Rev3.txt](Rev3.py)

**Hints**

What do you think the program is trying to accomplish? It is related to mathematics.

** Depending on the Python version, approach, processing strength, etc. Individuals may find varying runtimes. Your patience is appreciated. **

---

#### Solve

First step in reverse engineering is understanding the code, heres every step explained:

```python
import math
import hashlib
import sys

# The size of the arrays
SIZE = int(3e5)

# The verification key
VERIFY_KEY = "46e1b8845b40bc9d977b8932580ae44c"


# Function to multiply two sequences
def getSequence(A, B, n, m):

    # Initialize the answer array
    ans = [0] * (n + m - 1)

    # Iterate through the elements of A
    for x in range(n):

        # Iterate through the elements of B
        for y in range(m):

            # Add the product of the elements of A and B to the answer array
            ans[x + y] += A[x] * B[y]

    # Return the answer array
    return ans


# Initialize the two arrays
A = [0] * SIZE
B = [0] * SIZE

# Open the first file
document1 = open("Document 1.txt", "r")

# Read the numbers in the first file
nums1 = document1.readlines()

# Initialize an index
idx = 0

# Iterate through the numbers in the first file
for num in nums1:

    # Add the number to the first array
    A[idx] = int(num.strip())

    # Increment the index
    idx += 1

# Open the second file
document2 = open("Document 2.txt", "r")

# Read the numbers in the second file
nums2 = document2.readlines()

# Reset the index
idx = 0

# Iterate through the numbers in the second file
for num in nums2:

    # Add the number to the second array
    B[idx] = int(num.strip())

    # Increment the index
    idx += 1

# Get the sequence
sequence = getSequence(A, B, SIZE, SIZE)

# Initialize a variable to hold the value
val = 0

# Iterate through the elements in the sequence
for num in sequence:

    # Add the element to the value
    val = (val + num)

# Turn the value into a string
val = str(val)

# Hash the value
val_md5 = hashlib.md5(val.encode()).hexdigest()

# Check if the hash is equal to the verification key
if val_md5 != VERIFY_KEY:

    # If not, tell the user
    print("Wrong solution.")

    # Exit the program
    sys.exit(1)

# Tell the user that the solution is correct
else:

    # If the solution is correct, tell the user
    print("Correct solution.")

# Hash the value
key = str(hashlib.sha256(val.encode()).digest())

# Reset the flag
flag = ""

# Iterate through the characters in the hash
for x in key:

    # Check if the character is alphanumeric
    if x.isalpha() or x.isnumeric():

        # If so, add the character to the flag
        flag += x

# Add the flag formatting
flag = "ctf{" + flag + "}"

# Print the flag
print(flag)
```

what does it do in a nutshell?

it does complex mathematical operations on two arrays of 300,000 numbers, then checks if output matches the verification key, if it does, it prints the flag.
you can simply run it but it would take forever to finish (300,00^2) operations😳😳, so we need to optimize it, or figure out a way to get the flag manually without running it, or both.

so what it actually does is the `fft convolution algorithm`, which is a way to multiply two polynomials in *`O(nlogn)`* time, but it does it in the naive *`O(n^2)`* time.

so we just need to implement the `fft convolution algorithm` on the same input, and we can get the flag.

just replace the `getSequence` function with this:

[Solve.py](solve.py)

```python
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
    Thx ChatGPT 😊😄

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
```
