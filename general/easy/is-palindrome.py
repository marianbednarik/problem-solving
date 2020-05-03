"""

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

## Examples:
Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

## Follow up:
Coud you solve it without converting the integer to a string?

"""

import math


def isPalindrome(x: int) -> bool:
    x = str(x)
    return str(x[: math.ceil(len(x) / 2)]) == str(x[math.floor(len(x) / 2) :])[::-1]
