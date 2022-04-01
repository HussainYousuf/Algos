from functools import cache


def lcs(str1, str2):

    @cache
    def _lcs(str1, str2):
        if(not str1 or not str2):
            return ()
        _str1 = str1[1:]
        _str2 = str2[1:]
        if(str1[0] == str2[0]):
            res = max(_lcs(_str1, _str2), _lcs(_str1, _str2), key=len)
            res = (str1[0], *res)
            return res
        return max(_lcs(_str1, str2), _lcs(str1, _str2), key=len)

    return "".join(_lcs(str1, str2))


print(lcs("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA",
      "GTCGTTCGGAATGCCGTTGCTCTGTAAA"))


# print(lcs("ABCBDAB", "BDCABA"))
