
# favorite
# compress
# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.

# test_00:
# compress('ccaaatsss')
# // -> '2c3at3s'
# test_01:
# compress('ssssbbz')
# // -> '4s2bz'
# test_02:
# compress('ppoppppp')
# // -> '2po5p'
# test_03:
# compress('nnneeeeeeeeeeeezz')
# // -> '3n12e2z'
# test_04:
# compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
# // -> '127y'


def uncompress(s):
    answer = ""
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    start_of_num = 0
    end_of_num = 0
    num_to_iterate = 0

    for idx, char in enumerate(s):

        if char not in nums:
            end_of_num = idx
            num_as_string = s[start_of_num: end_of_num]
            num_to_iterate = int(num_as_string)

            for _ in range(num_to_iterate):
                answer += s[idx]

            start_of_num = end_of_num + 1

    return answer
