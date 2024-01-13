# compress
# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.

# compress('ccaaatsss') # -> '2c3at3s'
# compress('ssssbbz') # -> '4s2bz'
# compress('ppoppppp') # -> '2po5p'
# compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'
# compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy');
# # -> '127y'

def compress(s):
    i = 0
    j = 0
    count = 0
    compressed = []

    while j < len(s):
        if s[i] == s[j]:
            count += 1
            j += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(s[i])
            count = 0
            i = j
    if count > 1:
        compressed.append(str(count))
    compressed.append(s[i])
    return "".join(compressed)
