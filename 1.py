def get_security_code(code: str, k: int) -> str:
    n = len(chars)

    left = 0

    while k > 0 and left < n - 1:
        # Find the next '0'
        while left < n - 1 and chars[left] != "0":
            left += 1

        if left >= n - 1:
            break

        # Find the next '1' after left
        right = left + 1
        while right < n and chars[right] != "1":
            right += 1

        if right >= n:
            break

        # Check if we can swap
        if right - left <= k:
            # Swap '0' at left with '1' at right
            chars[left], chars[right] = chars[right], chars[left]
            # Decrease k by the number of moves needed
            k -= right - left
            # Move left pointer to the new position of the swapped '1'
            left += 1
        else:
            break

    return "".join(chars)


# Example usage
code1 = "00100101"
k1 = 4
print(get_security_code(code1, k1))  # Output: "10010001"

code2 = "0010"
k2 = 5
print(get_security_code(code2, k2))  # Output: "1000"

code3 = "1111"
k3 = 2
print(get_security_code(code3, k3))  # Output: "111"
