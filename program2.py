def decode_message(s: str, p: str) -> bool:
    # Initialize the DP table
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: empty string matches empty pattern
    dp[0][0] = True
    
    # Handle patterns starting with '*' (which can match empty string)
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                # '*' matches zero or more characters
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?':
                # '?' matches exactly one character
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Characters must match exactly
                dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
    
    # The result is whether the whole message matches the whole pattern
    return dp[len(s)][len(p)]

'''# Test cases
print(decode_message("aa", "a"))        # False
print(decode_message("aa", "*"))        # True
print(decode_message("cb", "?a"))       # False
print(decode_message("adceb", "*a*b"))  # True
print(decode_message("acdcb", "a*c?b")) # False'''
