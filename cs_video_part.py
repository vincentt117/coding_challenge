# https://app.codesignal.com/challenge/aesrryCpibT2mevy6

from fractions import Fraction as frac

def videoPart(part, total):
    part_int = int(part[:2]) * 3600 + int(part[3:5]) * 60 + int(part[6:])
    total_int = int(total[:2]) * 3600 + int(total[3:5]) * 60 + int(total[6:])
    res = frac(part_int, total_int)
    return [res._numerator, res._denominator]

