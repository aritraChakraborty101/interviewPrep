def caesarCipherEncryptor(string, key):
    k = key
    result = ""
    if k > 26:
        k = k % 26
    for i in string:
        temp = ord(i)
        if temp + k > ord('z'):
            num = ((temp + k) - ord('z'))
            result += chr((ord('a') - 1) + num)
        else:
            result += chr(temp + k)

    return result
