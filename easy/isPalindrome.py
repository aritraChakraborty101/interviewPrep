def isPalindrome(string):
    result = ''
    for i in range(len(string) - 1, -1, -1):
        result += string[i]

    if result == string:
        return True
    else:
        return False
