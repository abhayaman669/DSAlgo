"""
Write a program to rotate an array of size n by d elements

---------------

Input: [1, 2, 3, 4, 5, 6, 7]
Output: [3, 4, 5, 6, 7, 2, 1]
"""

def rotate(arr, d, n):
    """
    Function to rotate an array
    """

    return arr[d:] + arr[:d]


if __name__ == '__main__':
    arr = [i for i in range(1, 8)]
    res = rotate(arr, 2, len(arr))
    print(res)