def max_efficiency(parcel_weights):
    n = len(parcel_weights)
    # Memoization dictionary to store results of subproblems
    memo = {}

    def calculate_efficiency(left, right):
        # Base case: no parcels left
        if left > right:
            return 0
        # Check if result is already computed
        if (left, right) in memo:
            return memo[(left, right)]
        
        # Choose the left parcel and move the left pointer
        pick_left = parcel_weights[left] + calculate_efficiency(left + 1, right)
        # Choose the right parcel and move the right pointer
        pick_right = parcel_weights[right] + calculate_efficiency(left, right - 1)
        
        # Take the maximum of both choices
        max_eff = max(pick_left, pick_right)
        
        # Store the result in memoization dictionary
        memo[(left, right)] = max_eff
        return max_eff

    return calculate_efficiency(0, n - 1)

print(max_efficiency([4,4,8,5,3,2]))  # Output: 9
print(max_efficiency([2,1,8,5,6,2,4]))  # Output: 9