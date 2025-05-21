def is_Palindrome(s):
    s=s.lower()
    left=0
    right=len(s)-1

    while left < right:
        while left < right and not s[ left ].isalnum( ):
            left = left + 1

        while left < right and not s[ right ].isalnum( ):
            right = right - 1

        if s[ left ] != s[ right ]:
            return False
        left = left + 1
        right = right - 1


    return True


print(is_Palindrome(input()))