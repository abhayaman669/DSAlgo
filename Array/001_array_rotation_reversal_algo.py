"""
Write a program to rotate an array of size n by d elements using reversal
algorithm

---------------

- Seperate array into two part A = arr[:d] and B = arr[d:]
- Reverse A we get Ar
- Reverse B we get Br
- Reverse (ArBr) we get (ArBr)r which is expected

---------------

Input: [1, 2, 3, 4, 5, 6, 7]
Output: [3, 4, 5, 6, 7, 2, 1]
"""

def rotate(arr, d, n):
    """
    Function to rotate an array
    """

    # Dividing array into two part
    A = arr[:d]
    B = arr[d:]

    # Reversing A and B
    Ar = A[::-1]
    Br = B[::-1]

    # Reversing ArBr
    ArBr = (Ar+Br)[::-1]

    return ArBr


if __name__ == '__main__':
    arr = [i for i in range(1, 8)]
    res = rotate(arr, 2, len(arr))
    print(res)