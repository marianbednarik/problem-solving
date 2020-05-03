"""

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.

"""


def reverse(x: int) -> int:
    result = int((str(x)[1:] if x < 0 else str(x))[::-1]) * (-1 if x < 0 else 1)
    return result if result < pow(2, 31) - 1 and result > pow(-2, 31) else 0


assert 54321 == reverse(12345)
assert -54321 == reverse(-12345)
assert 0 == reverse(1234567899)
